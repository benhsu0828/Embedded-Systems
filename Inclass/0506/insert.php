<body>
<?php
$host = '172.20.10.4';                                                
$user = 'william';           
$passwd = '123';         
$database = 'test';       
$connect = new mysqli($host , $user , $passwd , $database);   

if ($connect->connect_error){                 
    die("連線失敗:".$connect->connect_error);           
}
else{
    $connect->query("SET NAMES 'UTF8'");                
    $C = $_GET["c"];                                        
    $F = $_GET["f"];
    $H = $_GET["h"];
    $D = $_GET["d"];
    $Insertsql = "INSERT INTO dhl (`Celsiu`,`Fahrenheit`,`Humidity`,`d`) VALUES ('$C' ,'$F','$H','$D')"; 
    $status = $connect->query($Insertsql);         
    // print($status);          
    if($D>50)
    {
        print("1");
    } 
    else
    {
        print("0");
    }                        
    // $selectSql = "SELECT * FROM dhl ";                  
    // $memberData = $connect->query($selectSql);          
    // if ($memberData->num_rows>0){                   
    //     while ($row = $memberData->fetch_assoc()){  
    //         print_r($row);
    //         // print_r($row['Time']);
    //         print_r($row['Celsiu']);
    //         print_r($row['Fahrenheit']);
    //         print_r($row['Humidity']);
    //         print_r($row['d']);
    //         echo '<br>';
    //     }
    // }else {
    //     echo '無資料';
    // }
    }
?>
</body>