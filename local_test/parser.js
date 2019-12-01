function myFunction $(temp) {
    var ddmmyyyy = /(?:[0-9]|[0-3][0-9])(?:[./-]|[\s])(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])[1-2][0-9][0-9][0-9]/i
    
    var mmddyyyy = /(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])[0-3][0-9](?:[./-]|[\s])[1-2][0-9][0-9][0-9]/i
    
    
    var ddmonthyy = /[0-3][0-9](?:[./-]|[\s])(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:[./-]|[\s])[0-9][0-9][\s]/i
    
    var ddmonthapoyy = /[0-3][0-9](?:[./-]|[\s]|)(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:[.'/-]|[\s])[0-9][0-9][\s]/i
    
    var ddmmyy = /(?:[0-9]|[0-3][0-9])(?:[./-]|[\s])(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])([0-9][0-9][\s])/i
    
    var ddmonthyyyy = /[0-3][0-9](?:[./-]|[\s])(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:[./-]|[\s])(?:[0-9][0-9][0-9][0-9]|[0-9][0-9])/i
    
    var mmddyy = /(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])[0-3][0-9](?:[./-]|[\s])([0-9][0-9])/i
    
    temp = "6/26/19"

    var t;
    if(temp.match(ddmmyyyy))
    {
        t = temp.match(ddmmyyyy);
    }
    else if(temp.match(mmddyyyy))
    {
        t= temp.match(mmddyyyy);
    }
    else if(temp.match(ddmmyy))
    {
        t= temp.match(ddmmyy);
    }
    else if(temp.match(mmddyy))
    {
        t= temp.match(mmddyy);
    }
    else if(temp.match(ddmonthyyyy))
    {
        t= temp.match(ddmonthyyyy);
    }
    else if(temp.match(ddmonthyy))
    {
        t= temp.match(ddmonthyy);
    }
    else if(temp.match(ddmonthapoyy))
    {
        t= temp.match(ddmonthapoyy);
    }
    else
    {
        t = "null"
    }    
     
    document.write(t[0]);
    }