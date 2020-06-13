<?php get_header(); ?>

  
  
 <!--ijaoover-->


    
    <div class="main2"> 
    
    
    <div class="leftmain5">
    <div class="news_show">
  
    
      <div class="about_wen2">

  
    
    <ul>
    
     <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
       <li>
             <a class="bt"> <h1><?php the_title(); ?>  </h1></a>
             <a class="time" href="#"><?php the_time('m-d-y') ?></a>
             <hr class="heng" />
          
            <div class="entry">
            <?php the_content(); ?>
			  
             </div>
           <!-- Baidu Button BEGIN -->
    <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">
        <a class="bds_qzone"></a>
        <a class="bds_tsina"></a>
        <a class="bds_tqq"></a>
        <a class="bds_renren"></a>
        <span class="bds_more">更多</span>
		<a class="shareCount"></a>
    </div>
<script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=875647" ></script>
<script type="text/javascript" id="bdshell_js"></script>
<script type="text/javascript">
	document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + new Date().getHours();
</script>
<!-- Baidu Button END -->
       <div class="in-di"><img src="<? bloginfo('template_url'); ?>/images/in_di.png" /></div>
       </li>
       
      
       <?php endwhile; ?>     
          
      



	<?php else : ?>
        
         
         
        <?php  endif; ?>   

         
    </ul>
            
             

  
  

         
     </div>
            

   </div>
     <div class="liuyan">

<?php comments_template(); ?>

				
		</div>		
    
    </div>
    
    
    
    <div class="rightmain2">
    <?php include_once("sidebar.php"); ?>
    <div class="coffi"><img src="<? bloginfo('template_url'); ?>/images/pages/coffie.png" /></div>
    </div>
   
   
   
   </div>
    
    
    
    
    </div>







<?php get_footer(); ?>
