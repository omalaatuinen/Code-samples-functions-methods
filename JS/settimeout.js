
( function ()// IIFE
{

	
    for (var i=1; i<= 4; i++)
    {
        (function (j) 
        {
        setTimeout (function ()
        {
            console.log(j);
        }, j*1000);
    })(i)
}



 }
)();
