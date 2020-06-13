<?php get_header(); ?>

  
  
 <!--ijaoover-->

    
    <div class="main2"> 
   
    
    <div class="leftmain5">
    <div class="news_show">
   
      <div class="about_wen2">

  
    
    <ul>
    
      <li>
     	<?php if (have_posts()) : ?>
            <h2 class="ar_bt">找到分类:<?php single_cat_title(); ?></h2>
 			<?php $post = $posts[0]; // Hack. Set $post so that the_date() works. ?>

			<?php /* If this is a category archive */ if (is_category()) { ?>
				<p>找到分类:<?php single_cat_title(); ?></p>

			<?php /* If this is a tag archive */ } elseif( is_tag() ) { ?>
				<p>找到标签：<?php single_tag_title(); ?></p>

		

			<?php /* If this is a paged archive */ } elseif (isset($_GET['paged']) && !empty($_GET['paged'])) { ?>
				<p>Blog Archives</p>
			
			<?php } ?>

			<?php include (TEMPLATEPATH . '/inc/nav.php' ); ?>
           <?php endif; ?>
           </li>
    
    
    
     <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
       <li>
             <a class="bt" href="<?php the_permalink() ?>"> <h1><?php the_title(); ?> </h1></a>
             <a class="time" href="#"><?php the_time('m-d-y') ?></a>
             <hr class="heng" />
             <?php the_post_thumbnail(); ?>
             <div class="entry">
			 <?php the_content(); ?>
             </div>
       
       <div class="in-di"><img src="<? bloginfo('template_url'); ?>/images/in_di.png" /></div>
       </li>
       
      
       <?php endwhile; ?>     
          
      



	<?php else : ?>
        <li>
         
         <p>SORRY,没有找到相关类容</p> 
         </li>
        <?php  endif; ?>   

         
    </ul>
            
             
    <div class="pager">   <?php par_pagenavi(); ?>  </div>
  
  

         
     </div>
            

   </div>
    
    
    </div>
    
    
    
    <div class="rightmain2">
    <?php include_once("sidebar.php"); ?>
    <div class="coffi"><img src="<? bloginfo('template_url'); ?>/images/pages/coffie.png" /></div>
    </div>
   
   
   
   </div>
    
    
    
    
    </div>







<?php get_footer(); ?>
