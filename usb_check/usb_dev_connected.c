#include <libusb.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define VENDOR_ID 0x0A4A
#define PRODUCT_ID 0xE1A2

int hotplug_callback(struct libusb_context *ctx, struct libusb_device *dev,
                     libusb_hotplug_event event, void *user_data) {
    static libusb_device_handle *dev_handle = NULL;
    struct libusb_device_descriptor desc;
    int rc;

    (void)libusb_get_device_descriptor(dev, &desc);

    if (LIBUSB_HOTPLUG_EVENT_DEVICE_ARRIVED == event) {
        rc = libusb_open(dev, &dev_handle);
        if (LIBUSB_SUCCESS != rc) {
            printf("Could not open USB device\n");
        }
    } else if (LIBUSB_HOTPLUG_EVENT_DEVICE_LEFT == event) {
        if (dev_handle) {
            libusb_close(dev_handle);
            dev_handle = NULL;
        }
    } else {
        printf("Unhandled event %d\n", event);
    }

    return 0;
}

int main(int argc, char *argv[]) {
    libusb_hotplug_callback_handle callback_handle;
    int rc;

    libusb_init_context(NULL, NULL, 0);

    rc = libusb_hotplug_register_callback(NULL, LIBUSB_HOTPLUG_EVENT_DEVICE_ARRIVED | LIBUSB_HOTPLUG_EVENT_DEVICE_LEFT,
                                          0, VENDOR_ID, PRODUCT_ID,
                                          LIBUSB_HOTPLUG_MATCH_ANY, hotplug_callback, NULL,
                                          &callback_handle);
    if (LIBUSB_SUCCESS != rc) {
        printf("Error creating a hotplug callback\n");
        libusb_exit(NULL);
        return EXIT_FAILURE;
    }

    while (1) {
        libusb_handle_events_completed(NULL, NULL);
        nanosleep(&(struct timespec){0, 10000000UL}, NULL);
    }

    libusb_hotplug_deregister_callback(NULL, callback_handle);
    libusb_exit(NULL);

    return 0;
}