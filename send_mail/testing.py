<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
<script type="text/javascript">
    
    function show(btnPan)
    
    {
        var docPan=document.getElementById('docPan');
        var docPan2=document.getElementById('docPan2');
        
        if (btnPan.value=="yes")
        {
            docPan.style.display="block"
            docPan2.style.display="block"
            btnPan.value="no"
        }
        else        
        
        {
            docPan.style.display="none"
            docPan2.style.display="none"
            btnPan.value="yes"
        }
    }


    function show2(btnAdr)
    {
        var docAdr=document.getElementById('docAdr')

        if (btnAdr.value=="yes"){

            docAdr.style.display="block"
            btnAdr.value="no"            
        }
        else{
            docAdr.style.display="none"
            btnAdr.value="yes"
        }
    }

</script>
</head>

<body>
    <div>Do you have Document?</div>
    <input type="button"  id="btnPan" value="yes" onclick="show(this)">

    <div id="docPan" style="display:none">
        Document No:
        <input type="text"  id="txtPan">
    </div>
    
    <div id="docPan2" style="display:none">
        Document No2:
        <input type="text"  id="txtPan2">

        <div> Do you have document3? </div>
        
        <input type="button" id="btnAdr" value="yes" onclick="show2(this)">

        <div id="docAdr" style="display:none">
        Adr no:
            
        <input type="text" id="txtAdr">
    
    </div>

    </div>

</body>

</html>