		<div id="footer">
             
             <div class="footer_main">
           
                      <div class="f_m">  
                          <div class="f_xian">
                           <div class="f_bq">
                               <div class="contact_wen2">
          <p>
         
          <b>电子邮件：</b><?php echo get_option('mytheme_mail'); ?>  &nbsp; &nbsp; &nbsp;  <b>QQ：</b><?php echo get_option('mytheme_qq'); ?> &nbsp; &nbsp; &nbsp; 
         
         </p>
          
          </div>
                           
                           
                           
                               <p>版权所有copy@<?php echo date("Y"); echo " "; bloginfo('name'); ?>&nbsp; &nbsp; 
                               <?php if (get_option('mytheme_beian')!=""): ?>
                              <?php echo get_option('mytheme_beian'); ?>
                              <?php else : ?>
                              </p>
                              <?php endif; ?>      
                               &nbsp; &nbsp;    
                            </div>
                            
   <div class="f_links">
                            
                               <li><h1>友情链接:</h1></li>
                              <?php wp_list_bookmarks('orderby=id&categorize=0&category=2&title_li='); ?>
                               <li> <a href="http://www.themepark.com">web主题公园</a></li>
                            </div>
                            </div>
                            
                       </div>
 <div style="display:none"><?php echo stripslashes(get_option('mytheme_analytics')); ?></div>
        
<script type="text/javascript" src="<?php bloginfo('template_url'); ?>/js/script.js"></script>
<script type="text/javascript"  charset=utf-8 src="<?php bloginfo('template_url'); ?>/js/lrscroll.js"></script> 
 <script type="text/javascript"  charset=utf-8 src="<?php bloginfo('template_url'); ?>/js/xuant2.js"></script>        
        
			
	



	<?php wp_footer(); ?>
	
	<!-- Don't forget analytics -->
	
</body>

</html>