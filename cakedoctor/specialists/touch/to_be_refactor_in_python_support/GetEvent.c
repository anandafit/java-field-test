/* Through this source code, you could see the point output architechture of touch device.
You could follow below code to do point parsing. And develop your own app. */

/**
Use the following command to build the "GetEvent" application
 -- gcc -o GetEvent GetEvent.c -lm
**/

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <limits.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <math.h>
#include <syslog.h>

#include <linux/input.h>

/*Note: If you couldn't build this source code successfully, it may caused by the old kernel issue.
Please enable below define depending on your kernel version */

#define MAX_DATAVAN_TOUCH  32768
#define MAX_V3_TOUCH 4096

#define MAX_MAIN_X 1024
#define MAX_MAIN_Y 768

#define MAX_CTD_X 800
#define MAX_CTD_Y 600

static int max_x = MAX_MAIN_X;
static int max_y = MAX_MAIN_Y;
static int max_input = MAX_DATAVAN_TOUCH;
static char strPOSDisplay[64] = { 0 };

typedef struct tagevent
{
    struct timeval time;
    unsigned short type;
    unsigned short code;
    int value;
} input_event;

void ParseEvent( input_event ev)
{
    static unsigned short X, Y, State;
    static unsigned short X2, Y2, State2;
    static unsigned char bIsSecond;


	if( ev.type == EV_ABS ) {
        switch( ev.code ) {
			case ABS_X: 
				syslog(LOG_INFO, "[%s][ABS_X] == %4f\n",strPOSDisplay, round((ev.value * max_x) /max_input));
				break;
			case ABS_Y: 
				syslog(LOG_INFO, "[%s][ABS_Y] == %4f\n",strPOSDisplay, round((ev.value * max_y) /max_input));
				break;

			default:
				break;
        }
    }
}

int main( int argc, char **argv )
{
    int fd;
    unsigned char byFlag = 0; /* 0: Point */
    char strPort[64] = { 0 };
    char strPOSDevice[64] = { 0 };
    fd_set readfds;

    openlog("[TOUCHMON]", LOG_NDELAY, LOG_DAEMON);

    if( argc == 1 || argc > 4 ) {
        syslog(LOG_INFO, "Touch input and device type is wrong");
        return 0;
    }

    sprintf(strPOSDisplay, "%s", "MAIN\0");
	
    sprintf( strPort, "%s", argv[1] );

    if(argc > 2)
     sprintf( strPOSDevice, "%s", argv[2]);

    if(argc > 3) {
     memset( strPOSDisplay, 0x00, 64 );
     sprintf( strPOSDisplay, "%s", argv[3]);
 
    }

    syslog(LOG_INFO," Event Port = %s ", strPort);

    if(strcmp(strPOSDevice,"DATAVAN") == 0 ){
      max_input = MAX_DATAVAN_TOUCH;
    } else if(strcmp(strPOSDevice, "V3") == 0) {
      max_input = MAX_V3_TOUCH;
    } else {
    }

    if(strcmp(strPOSDisplay, "CTD") == 0 ) {
      max_x = MAX_CTD_X;
      max_y = MAX_CTD_Y;
    }
    
    syslog(LOG_INFO, "MAX_X == %4d\n", max_x);
    syslog(LOG_INFO, "MAX_Y == %4d\n", max_y);
    syslog(LOG_INFO, "MAX_INPUT == %4d\n", max_input);
    fd = open(strPort, O_RDONLY );
    if( fd >= 0 ) {	
        syslog(LOG_INFO, "%s device open successfully", strPort);
        FD_ZERO( &readfds );
        FD_SET( fd , &readfds );
        while( 1 ) {
            if( select( fd+1, &readfds, NULL, NULL, NULL ) > 0 ) {
                input_event ev;
                if( sizeof( input_event ) == read( fd, &ev, sizeof( input_event ) ) ) {
                    ParseEvent( ev );
                }
            }
        }	
    }
    syslog(LOG_INFO, "%s device opening failed", strPort);
    closelog();
    return 0;
}
