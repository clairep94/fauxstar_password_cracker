## INTRO ART ---------------------------------------------------#
intro_ascii = '''

▄████  ██     ▄       ▄         ▄▄▄▄▄      ▄▄▄▄▀ ██   █▄▄▄▄ 
█▀   ▀ █ █     █  ▀▄   █       █     ▀▄ ▀▀▀ █    █ █  █  ▄▀ 
█▀▀    █▄▄█ █   █   █ ▀      ▄  ▀▀▀▀▄       █    █▄▄█ █▀▀▌  
█      █  █ █   █  ▄ █        ▀▄▄▄▄▀       █     █  █ █  █  
 █        █ █▄ ▄█ █   ▀▄                  ▀         █   █   
  ▀      █   ▀▀▀   ▀                               █   ▀    
        ▀                                         ▀         

█ ▄▄  ██      ▄▄▄▄▄    ▄▄▄▄▄    ▄ ▄   ████▄ █▄▄▄▄ ██▄   
█   █ █ █    █     ▀▄ █     ▀▄ █   █  █   █ █  ▄▀ █  █  
█▀▀▀  █▄▄█ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄  █ ▄   █ █   █ █▀▀▌  █   █ 
█     █  █  ▀▄▄▄▄▀   ▀▄▄▄▄▀   █  █  █ ▀████ █  █  █  █  
 █       █                     █ █ █          █   ███▀  
  ▀     █                       ▀ ▀          ▀          
       ▀                                                
▄█▄    █▄▄▄▄ ██   ▄█▄    █  █▀ ▄███▄   █▄▄▄▄            
█▀ ▀▄  █  ▄▀ █ █  █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀            
█   ▀  █▀▀▌  █▄▄█ █   ▀  █▀▄   ██▄▄    █▀▀▌             
█▄  ▄▀ █  █  █  █ █▄  ▄▀ █  █  █▄   ▄▀ █  █             
▀███▀    █      █ ▀███▀    █   ▀███▀     █              
        ▀      █          ▀             ▀               
              ▀                                         
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
'''


## INTRO BLURB -----------------------------------------------------#
intro_blurb = '''
Welcome to the FAUX-STAR PASSWORD CRACKER.

This program contains several attack methods used by hackers to gain access to victims' account information.
These attacks exploit common password practices, as well as social engineering tactics, and this program demonstrates
these exploits to encourage safer password practices. 


/////////////////////////////////////////////////////////////////

'''

## ATTACK OPTIONS --------------------------------------------------#
attack_options_blurb = '''

/////////////////////////////////////////////////////////////////


What would you like to do?

PREP ATTACKS:
1. Launch Phishing Site "Faux-Star"
2. Add to Program's 'Common Passwords' Data

ATTACKS:
3. Dictionary Attack (3 data files available)
4. Standard Brute Force Attack 
5. Hashcat Mask Attack
6. L33tspeak Attack (3 data files available)
7. Hashcat Hybrid Attack (3 data files available)

Please enter the option number (1-7): 
>>> '''

####------------- PHISHING --------------------------####

phishing_email = '''

/////////////////////////////////////////////////////////////////


The following email has been sent to your target with a link to the
FAUX STAR PASSWORD CRACKER:

Subject: From Co-Star -- A Gift for You for Being an Integral Part of Our Cosmic Community!

Hi!

On behalf of the team at Co-Star, we want to say thank you for being part of our community.
We are always trying to improve our app and we are excited to announce that we are developing a
new 'Love-Compatibility' feature! We have selected you to be one of our beta-testers. Please click
the link below to test the feature, and be entered for a chance to win a £100 giftcard as a token
of our appreciation.

LINK

Thanks and love always,
Co-Star team
'''


## PASSWORD NOT FOUND --------------------------------------------------#
password_not_found_blurb = f'''

/////////////////////////////////////////////////////////////////


Password not found.
Please select another attack.
'''


## PASSWORD FOUND --------------------------------------------------#
password_found_blurb = f'''

/////////////////////////////////////////////////////////////////


The target's password has been found.
The password is:
'''