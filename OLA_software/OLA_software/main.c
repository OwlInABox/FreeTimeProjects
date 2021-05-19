/*
 * OLA_software.c
 *
 * Created: 21/02/2020 08:44:43
 * Author : nico835t
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include "setup.h"




int main(void)
{
    
	
	interruptSetup();
	registerSetup();
    while (1) 
    {
	
    }
}
