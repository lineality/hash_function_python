from datetime import datetime
# get time
timestamp_raw = datetime.utcnow()
# make readable string
timestamp = timestamp_raw.strftime('%Y%m%d%H%M%S%f')

def make_hash(input_string, timestamp_string):
    """
    designed to be a good-enough hash, not relying on libraries
    that includes string and timestamp

    the timestamp kind of functions as a 'secret key'
    as in crypographic 'signing' and verification
    again: not meant to be super world class,
    but light weight and easy to debug,
    not likely to have unexpected or incomprehensible issues
    no external libraries, trust issues, etc. 
    
    the first few digits are less random, so -> removed
    this also keeps the hash from getting huge so quickly

    to make the numbers more significantly different if even one
    input character is changed: add an additional hash if the 
    current hash is odd/even (even picked here)

    for timestamp: use this to get sub-second depth in a string

    from datetime import datetime
    # get time
    timestamp_raw = datetime.utcnow()
    # make readable string
    timestamp = timestamp_raw.strftime('%Y%m%d%H%M%S%f')

    """

    string_to_hash = input_string + timestamp_string

    hash = 1
    for this_character in string_to_hash:
        # 31 or 101 are recommended

        """
        Smaller-Number Version
        """
        # hash = ( 101 * (1/hash) ) + ord(this_character)

        """
        Larger-Number Version
        """
        hash = 101 * (hash + ord(this_character))
        
        """
        odd even: reflip
        if the hash is even: hash again
        """
        if not hash%2:
            hash = 101 * (hash + ord(this_character))

        if len(str(hash)) > 6:
           hash = str(hash)[2:]

        hash = int(hash)
        
        # # the story so far...
        # print(ord(this_character))
        # print(timestamp)
        # print(hash)

    # print(timestamp)

    hash = str(hash)

    # edge case: if the decimal point shows up
    hash = hash.replace(".","")

    # edge case: if the number is short
    # if len(hash) > 12:
    #     hash = str(hash)[1:]

    return hash

# Run it
print( make_hash("123:123:243:234", timestamp) )

# compare small change: just the last digit of the time
print( make_hash("123:123:243:234","20221008133518385205") )
print( make_hash("123:123:243:234","20221008133518385206") )

# small number input: edge case check
print( make_hash("1","3") )
