


	<DIV id="imgPlay2">
	<!-- Thumbnails -->
    <div class="gundong">
     <ul class="imgs" id="actor2">
	<?php foreach ( $images as $image ) : ?>

				<?php if ( !$image->hidden ) { ?>
               
				<li><img title="<?php echo $image->description ?>" alt="<?php echo $image->alttext ?>" src="<?php echo $image->imageURL ?>"/>
                 <p class="description"><?php echo $image->description ?></p> 
                </li>
			   
            	<?php } ?>


 	<?php endforeach; ?>
 	</ul>
    </div>

    <DIV class=prev2></DIV>
    <DIV class=next2></DIV>
    </DIV>


