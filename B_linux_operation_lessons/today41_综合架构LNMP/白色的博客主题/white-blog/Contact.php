<?php  
/* 
Template Name:Contact
*/  
?> 


<?php get_header(); ?>
<style type="text/css">
    html,body{margin:0;padding:0;}
    .iw_poi_title {color:#CC5522;font-size:14px;font-weight:bold;overflow:hidden;padding-right:13px;white-space:nowrap}
    .iw_poi_content {font:12px arial,sans-serif;overflow:visible;padding-top:4px;white-space:-moz-pre-wrap;word-wrap:break-word}
</style>
<script type="text/javascript" src="http://api.map.baidu.com/api?key=&v=1.1&services=true"></script>


<div class="maim_pages">
   <div class="main5" style="background:#FFF;"> 

     

 
 
 
 
       <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
      <div class="about_wen2" >
     
    
    
      
      
       <?php the_content(); ?>
       </div>
       <?php endwhile; endif; ?>

      <div class="liuyan" style="float:none;">

<?php comments_template(); ?>

				
		</div>		

     
     </div>
    <img class="shadow_2" src="<? bloginfo('template_url'); ?>/images/pages/shadouw.png" />
   
   
   </div>
</div>



<?php get_footer(); ?>
