// TABLE 2 (adaptive) //==============================================

    var $thn_index, 
        $thn_html, 
        $table_name = $('.table2');

    $table_name.children(":first-child").children().children().each(function () {
        $thn_html = $(this).html();
        $thn_index =  $(this).index();
        //console.log('index: '+thn_index+' text: '+thn_html);

        $table_name.children().children().each(function () {
            $(this).children().eq($thn_index).attr('data-thn', $thn_html);
        });
    });





  
  var $last_win_w = $(window).width();     
 
  $(window).on("resize", function () {
       
      
        if ($(window).width() != $last_win_w) {
          
          var $table_w =        Math.round($table_name.width());
          
          console.log($table_w);
          
          if($table_w <= 720){
            $table_name.addClass('resp1');
          }
          else{
            $table_name.removeClass('resp1');
          }
          
          if($table_w <= 480){
            $table_name.addClass('resp2');
          }
          else{
            $table_name.removeClass('resp2');
          }
          
          
          $last_win_w = $(window).width();
          
        }
    });
