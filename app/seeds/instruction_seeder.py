from app.models import db, Instruction

def seed_instructions():

    bird_project1= Instruction(
        projectId=1,
        stepOrder=1,
        stepTitle="Get materials",
        instructions="Gather your materials", 
        photoUrl="https://imgprd19.hobbylobby.com/2/0e/4f/20e4f0a77628cacbbbb622fb4a01f7728b821d88/350Wx350H-116392-1019-px.jpg", 
        videoUrl="Video of materials"
    )

    bird_project2= Instruction(
        projectId=1,
        stepOrder=2,
        stepTitle="Start square",
        instructions="Take two pieces of wood and use wood glue put the two together", 
        photoUrl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbYADPGL1BShmV9Nw9K12GCVu5SAR1pZ_0cBKV9AYyaakIoj-rZMdQF2cDIkWaM15sIGA&usqp=CAU", 
        videoUrl="Video of the action"
    )

    bird_project3= Instruction(
        projectId=1,
        stepOrder=3,
        stepTitle="Add rest of square",
        instructions="Repeat step 2 with the last two pieces of the square", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project4= Instruction(
        projectId=1,
        stepOrder=4,
        stepTitle="Add Roof",
        instructions="Add roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project5= Instruction(
        projectId=1,
        stepOrder=5,
        stepTitle="Add Shingles",
        instructions="Add shingles to roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action",
    )

    casino_clock1=Instruction(
        projectId=2,
        stepOrder=1,
        stepTitle="3D Print",
        instructions="""
                        3D print of parts for a single unit.
                        Print them with supplied posture.
                        Support structure is not necessary to print.
                        Print 14 copies of hinge.stl.
                        Parts for a single unit can be printed out with common 200mm x 200mm 3D printer.
                        Remove debris and blobs around the printed parts.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FZ6/C95S/KZBA6KQC/FZ6C95SKZBA6KQC.jpg?auto=webp&frame=1&width=775&height=1024&fit=bounds&md=76ba8aa9d6423ad5086e4b12e9ba2495",
        
    )

    casino_clock2=Instruction(
        projectId=2,
        stepOrder=2,
        stepTitle="Assemble the Rotor",
        instructions="""
                        The process of assembly is also illustrated in the video above.

                        Before attaching the card holder (hinge), please make sure that the card can be inserted smoothly.
                        Attach the hinge to the rotor by snap-fit manner.
                        Please note that the hinge has front and back. Please check the figure above.
                        After attaching the hinge, confirm the smoothness of the hinge. Rubbing (frequent motion of hinge with some strong force) might make it smooth.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F8U/YRNB/KZBA6L77/F8UYRNBKZBA6L77.jpg?auto=webp&frame=1&crop=3:2&width=800&height=1024&fit=bounds&md=ae112a8a15850210f592c943c0233c9f",
    )

    casino_clock3=Instruction(
        projectId=2,
        stepOrder=3,
        stepTitle="Attach the Motor",
        instructions="""
                        Attach the motor with two tapping screws.
                        Cables should be drawn to backward.
                        Fix cables with zip ties.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F8T/IZTV/KZBA6LRP/F8TIZTVKZBA6LRP.jpg?auto=webp&frame=1&crop=3:2&width=600&fit=bounds&md=83b58c6f9307531f255b70f949e62138",
    )

    casino_clock4=Instruction(
        projectId=2,
        stepOrder=4,
        stepTitle="Attach the Rotor to the Motor",
        instructions="""
                        Push in the axis of the motor to the hole of the rotor.
                        if they are loose, one drop of superglue from the outer hole will fix it.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FZ0/86KQ/KZBA6LZO/FZ086KQKZBA6LZO.jpg?auto=webp&frame=1&width=1024&fit=bounds&md=11f72f8d2c55555234d598a81e761b6b",
    )      

    casino_clock5=Instruction(
        projectId=2,
        stepOrder=5,
        stepTitle="Attach Cards",
        instructions="""
                        Stick double-sided adhesive tape to the short edge of the card.
                        Slide-in the card to the channel of the card holder (hinge).
                        1-2mm gap between the cards to the pillar is ideal.
                        You can arrange the cards either randomly (for fun) or ordered (less noise). Please note that the rotor rotates CW.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FAX/9GKB/KZBA6M8Q/FAX9GKBKZBA6M8Q.jpg?auto=webp&frame=1&crop=3:2&width=652&fit=bounds&md=93aa4d89772da241f5a9d7b96908a5b9",
    )  

    casino_clock6=Instruction(
        projectId=2,
        stepOrder=6,
        stepTitle="Make 3 Units Getting Together",
        instructions="""
                        Print base.stl and attach the units to the base.
                        Attach motor driver to the base.
                        (optional : cover.stl can be used in the final step. If you use Dupont connectors, the cover.stl is too small to cover them. To use this cover, direct soldering of the wires are necessary. M5stack can be attached with a M2 screw.)
                    """,
        photoUrl="https://content.instructables.com/ORIG/FJQ/ZFOH/KZBA6NQ0/FJQZFOHKZBA6NQ0.jpg?auto=webp&frame=1&width=717&height=1024&fit=bounds&md=6201514dc2ca3520295f5b8a4e1ce2cf",
    )           

    casino_clock7=Instruction(
        projectId=2,
        stepOrder=7,
        stepTitle="Connect Microcontroller",
        instructions="""
                        Selection of microcontrollers

                        You can use any micro controller with 12 or more GPIO ports to control three stepper motors.
                        The clock code with WiFi time acquisition assumes ESP8266 / ESP32 type modules.
                        I used M5stamp-C3 for this clock.

                        Connection example of M5stamp-C3

                        Connect four pins of first (1minute) motor to G4, G5, G6, G7.
                        Connect four pins of second (10minute) motor to G0, G1, G8, G10.
                        Connect four pins of third (hour) motor to G9, G18, G19, G21.
                        Connect 5V and GND to the microcontroller. (M5stamp-C3 has three 5V and GND pairs)
                    """,
        photoUrl="https://content.instructables.com/ORIG/FJQ/ZFOH/KZBA6NQ0/FJQZFOHKZBA6NQ0.jpg?auto=webp&frame=1&width=717&height=1024&fit=bounds&md=6201514dc2ca3520295f5b8a4e1ce2cf",
    )       


    casino_clock8=Instruction(
        projectId=2,
        stepOrder=8,
        stepTitle="Edit Source Code and Flash",
        instructions="""
                        Test

                        Two types of test codes are provided : for a single unit or three units.
                        Register the order of the cards to the source code.
                        If you use microcontrollers other than M5stamp, edit the port assignment.
                        Flash the code using Arduino IDE.
                        Confirm the correctness of card order by using single-unit-test.ino before using clock.ino because the clock code so too slow to check the correctness.

                        Use as clock

                        Copy the card order definition from the test code to clock.ino.
                        Flash clock.ino to the microcontroller with Arduino IDE.

                        SSID / password configuration using SmartConfig

                        You can set SSID and password of your WiFi using smartphone app.This function is named SmartConfig. The apps for setting are at

                        Android : https://play.google.com/store/apps/details?id=com.khoazero123.iot_esptouch_demo
                        iOS : https://apps.apple.com/jp/app/espressif-esptouch/id1071176700
                        Please not that your smartphone should be connected to 2.4GHz WiFi.

                        LED colors on M5stamp

                        green : initializing the rotors
                        blue : connecting WiFi stored in non-volatile memory
                        red : smartConfig mode. Please set SSID and password using smartConfig app.
                        turn off : clock operation mode
                    """,
        photoUrl="https://content.instructables.com/ORIG/FVS/QB7W/KZBA6P9G/FVSQB7WKZBA6P9G.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=0052fd3109d6441894a67cb55f5e5989",
    )    

    one_board_mug1=Instruction(
        projectId=3,
        stepOrder=1,
        stepTitle="Measure the Circles",
        instructions="""
                        Use any circular shape you wish or measure using a compass. 
                        Create an outter circle and an inner circle. 
                        Sizes can very but keep in mind this is the size of the lip of the mug you will drink from. 
                        (Also keep in mind some sanding will take place)

                        I make most mugs out of 5/6 circles with one bottom I’ll add later.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F9G/3GTT/KZBA1FUQ/F9G3GTTKZBA1FUQ.jpg?auto=webp&frame=1&fit=bounds&md=7ef820df5c39c993cadfe3630dc4569f",
    )
    
    one_board_mug2=Instruction(
        projectId=3,
        stepOrder=2,
        stepTitle="Cut Out",
        instructions="""
                        Start by drilling a hole in the center of the mug. Cut out inside first. Then cut outside ring.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FWV/6KID/KZBA1FUV/FWV6KIDKZBA1FUV.jpg?auto=webp&frame=1&width=634&height=1024&fit=bounds&md=7cd60a18426ba1dd890929772d970a4d",
    )

    one_board_mug3=Instruction(
        projectId=3,
        stepOrder=3,
        stepTitle="Glue Together",
        instructions="""
                        Glue all pieces together and clamp. (Do not add bottom of mug yet)

                        If you do not have any clamps you can simply stack something heavy on top such as a weight or rocks.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FWV/6KID/KZBA1FUV/FWV6KIDKZBA1FUV.jpg?auto=webp&frame=1&width=634&height=1024&fit=bounds&md=7cd60a18426ba1dd890929772d970a4d",
    )

    one_board_mug4=Instruction(
        projectId=3,
        stepOrder=4,
        stepTitle="Begin to Sand",
        instructions="""
                        You can use any sanding method. Some work faster than others. Sand with a low grit 60/80 to shape the mug. Use a large spindle sander for inside of a dremel.
                    """,
    )

    one_board_mug5=Instruction(
        projectId=3,
        stepOrder=5,
        stepTitle="Add Bottom",
        instructions="""
                        Once sanded to your likening, trace the bottom of mug on remaining wood. Cut out with Scroll saw and glue to mug. Once dry, sand again.
                    """,
    )

    one_board_mug6=Instruction(
        projectId=3,
        stepOrder=6,
        stepTitle="Handle",
        instructions="""
                        On remaining wood, measure height of mug and draw a handle you desire. Cut out and glue to mug. Clamp or secure and allows to dry.

                        You can also use dowel pins for extra hold.

                        You may need to use dremel or hand sand a curve in the handle ends to allow a closer fit to the mug.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FI5/3OWK/KZBA1FVQ/FI53OWKKZBA1FVQ.jpg?auto=webp&frame=1&width=575&height=1024&fit=bounds&md=bf508a2da6e1a63aa99b16e9cd427258",
    )

    one_board_mug7=Instruction(
        projectId=3,
        stepOrder=7,
        stepTitle="Finish Handle",
        instructions="""
                        Sand handle once dry.

                        I like to use strips of sand paper used with a lathe. This helps develop a more rounded look.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FY7/RL1L/KZBA1FV1/FY7RL1LKZBA1FV1.jpg?auto=webp&frame=1&fit=bounds&md=58ca0d08649fea49699de4b7e5f1508c",
    )

    one_board_mug8=Instruction(
        projectId=3,
        stepOrder=8,
        stepTitle="Add Finish",
        instructions="""
                        I usually test in water at this point. If you have any leaks you can soak the wood in water and allow to dry. This helps shrink the wood.

                        You can also add a food safe epoxy to the inside to seal any leaks or to allow for both cold and hot beverages. You can even use coffee for more natural looks.

                        Before sealing add any design you wish. Torched, stained etc.

                        Add wood oil and wood conditioner to outside of mug to seal.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F6Y/R6JL/KZBA1FWJ/F6YR6JLKZBA1FWJ.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d7af5ae887c84c5cf35e99f3b9a6b359",
    )

    one_board_mug9=Instruction(
        projectId=3,
        stepOrder=9,
        stepTitle="Allow Any Finishes to Cure",
        instructions="""
                        Allow the cure per instructions on product used.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FIC/RO72/KZBA1FWK/FICRO72KZBA1FWK.jpg?auto=webp&frame=1&fit=bounds&md=ef5c95a65c5263252bb3002ab3fa9fb1",
    )

    one_board_mug10=Instruction(
        projectId=3,
        stepOrder=10,
        stepTitle="Use Remaining Pieces of Wood",
        instructions="""
                        Just so we have no waste, you can use the inner circles you cut out and make a smaller mug. A shot glass or juice glass. Follow the same steps!! Then enjoy!!!
                    """,
        photoUrl="https://content.instructables.com/ORIG/FM1/8EYX/KZBA1FVG/FM18EYXKZBA1FVG.jpg?auto=webp&frame=1&width=628&height=1024&fit=bounds&md=2b3645e2db53a0024796989cee81dc7f",
    )

    skillet_burger1=Instruction(
        projectId=4,
        stepOrder=1,
        stepTitle="Fry Up the Bacon",
        instructions="""
                        In a large saute pan over medium-high heat, add bacon. Cook until crispy and remove to a paper towel covered plate. Reserve bacon grease.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FG7/M0DL/KYK4NWC1/FG7M0DLKYK4NWC1.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=727e24ebd9fc48457c55b2e452da9220",
    )

    skillet_burger2=Instruction(
        projectId=4,
        stepOrder=2,
        stepTitle="Get the Onions Going",
        instructions="""
                        Add sliced onions to bacon grease and cook for 3 minutes stirring occasionally.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FG7/M0DL/KYK4NWC1/FG7M0DLKYK4NWC1.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=727e24ebd9fc48457c55b2e452da9220",
    )

    skillet_burger3=Instruction(
        projectId=4,
        stepOrder=3,
        stepTitle="Make the Patties",
        instructions="""
                        Add patty ingredients to a mixing bowl and combine. Form into 6 patties. Add to saute pan with onions. Reduce heat to medium. Cover pan and cook for 8 minutes.

                        Flip each burger and recover for 8 minutes more.

                        Remove lid and lay a slice of cheese on each burger. Let sit for a minute then remove burgers. Remove onions from heat.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FYD/WV95/KYK4NWBZ/FYDWV95KYK4NWBZ.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=f8d508e203d652b1b506abc1d36d999b",
    )

    skillet_burger4=Instruction(
        projectId=4,
        stepOrder=4,
        stepTitle="Make the Sauce",
        instructions="""
                        Combine sauce ingredients in a small bowl and set aside.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FHE/ACCO/KYK4NWBT/FHEACCOKYK4NWBT.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=2c457488b792655c263a91f32ad45dc8",
    )

    skillet_burger5=Instruction(
        projectId=4,
        stepOrder=5,
        stepTitle="Build the Burger",
        instructions="""
                        Build the burger: smear bun with sauce. Add pickles and bacon. Top with a cheeseburger and cooked onions. Add top bun and enjoy!
                    """,
        photoUrl="https://content.instructables.com/ORIG/FEA/B667/KYK4NWBY/FEAB667KYK4NWBY.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=c184318d11bd6c0378b95837fbd25fb4",
    )

    james_webb1=Instruction(
        projectId=5,
        stepOrder=1,
        stepTitle="Layout and Outline the Golden Hexagons",
        instructions="""
                        The first step is to lay the golden hexagon stickers out in the pattern shown in the image to resemble the telescope's mirror. Do not stick the hexagons to the wood, simply lay them on there.

                        Using the pencil you then need to draw an outline around the stickers.

                        Once this outline is done you then need to draw another outline 2cm larger than the one you just did. I did this by using the ruler to make a small mark 2cm out from each flat edge and then draw a straight line parallel to the previous outline
                    """,
        photoUrl="https://content.instructables.com/ORIG/FOA/PHZ3/KYK4QAOS/FOAPHZ3KYK4QAOS.jpg?auto=webp&frame=1&width=719&fit=bounds&md=b8dde0a898fad98e8dae2b7df4785fec",
    )

    james_webb2=Instruction(
        projectId=5,
        stepOrder=2,
        stepTitle="Cut, Sand and Paint the MDF",
        instructions="""
                        First, cut around the outer line you have drawn on the wood with the pencil using a Jigsaw (other tools may be better but a Jigsaw is what I had to hand). Then drill a hole in the center circle that was drawn for the clock and use the jigsaw to cut the circle out. When cutting the hole make sure you stay on the inside of the line so the clock fits snug into the hole without any glue. You should end up with the shape shown in the picture.

                        Once the MDF has been cut, take the sandpaper (i used P120 but that may not be the optimal grit size) and sand all the edges of the MDF and the middle. As you are sanding the middle circle, make sure the clock fits tightly in the hole as you go, that way you will get a good fit won't need any glue when fitting the clock.

                        Once all the edges have been sanded, brush off any unwanted sawdust and place it in the paint area.

                        The paint area doesn't need to be indoors however protection from weather may be necessary as the paint takes an hour or so to dry properly. I painted mine on bin bags placed on the lawn as it was a sunny winter's day when I painted it.

                        Make sure you keep the spray can at least 25cm away from the MDF when spraying to prevent drips from forming.

                        Also, remember to spray the edges of the MDF as these will be visible when it is hanging on the wall. There is no need to do the backside of the MDF unless you want to.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FZ3/67BZ/KYVK6ZK4/FZ367BZKYVK6ZK4.jpg?auto=webp&frame=1&width=746&height=1024&fit=bounds&md=f328dbec2577deea8d055990585adfdc",
    )

    james_webb3=Instruction(
        projectId=5,
        stepOrder=3,
        stepTitle="Stick the Hexagons on the MDF and Fit the Clock",
        instructions="""
                        Sticking the Hexagons Down
                        Sticking the hexagon panels on the MDF is as simple as peeling the sticky side cover off and applying to the painted side of the MDF.

                        To get the alignment right (as all the hexagons will be slightly different in size) i suggest arranging the hexagons where they are going to be stuck down before sticking them, that way you can make sure they align correctly before committing. This can be cumbersome as the panels slide easily on the wood but it is worth spending the time on.

                        Once they are all aligned, work your way from bottom to top or top to bottom sticking one panel down at a time.

                        The panels can be removed once stuck down and won't peel the paint off (at least in my experience) but you will need a knife to get them off.

                        Once all panels have been stuck down, peel the protective film off the shiny side to reveal the golden majesty :)

                        Fitting the Clock
                        If you have cut and sanded the hole to a snug size you should just be able to push the clock enclosure into the hole without any glue. If the hole is too big then you may need some sort of glue to hold it in place.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FNC/JKOF/KYVK71DG/FNCJKOFKYVK71DG.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=83de509cec2e66f4e86e07ae4a6fd110",
    )

    james_webb4=Instruction(
        projectId=5,
        stepOrder=4,
        stepTitle="Mounting",
        instructions="""
                        If you bought the suggested clock, the clock mechanism itself has a hook for hanging the clock. Providing that you made the clock fit tightly into the hole, you can use the hook with a nail or a standard picture hook.

                        The other option is to use hanging strips. It is important to use the velcro(esk) ones to make the clock sit slightly off the wall as the MDF might bend slightly and therefore fail to stick (see suggested hanging methods in the Supplies section.

                        THAT'S IT!!

                        Hope you enjoy your new James Webb Space TeleClock
                    """,
        photoUrl="https://content.instructables.com/ORIG/F2D/W1UN/KYVK737V/F2DW1UNKYVK737V.jpg?auto=webp&frame=1&width=924&height=1024&fit=bounds&md=cf297c9c91d3ecf32bee622b0f5bff2f",
    )

    slowmo_bird1=Instruction(
        projectId=6,
        stepOrder=1,
        stepTitle="The Set-up",
        instructions="""
                        This project involves carefully planning of the arrangement of objects in space. First, you need a bird feeder. You may already have one, but make sure it is placed in an optimal location, typically near a large window of your dwelling. Place a perch 8 to 10 feet away from the feeder, opposite the direction of the house and somewhat off to the side. This plan takes advantage of the fact that birds like to land near a feeder and check it out before flying to it and consuming the seed. Photograph the bird when it flies from the perch to the feeder.

                        The type of feeder doesn't matter much. I use only sunflower seed in my feeder, as most birds really don't care for the other seeds in mixed bird feed. I also use a suet feeder, which is a great way to attract woodpeckers.

                        It's best to use a natural stick, such as one that's fallen from a tree. You can jam it into the ground or use a support like an umbrella stand to hold it up. The top of it should be about the same height as the bird feeder. By using a natural stick rather than a human-made object, you can get natural-looking photos of a perching bird if you want them. You may need to move it around to find the spot that the birds prefer. It's also better if there are not competing objects that can be used as perches nearby. Finally, try to use a location that will result in photographs with a pleasing background.

                        Inside the house, place your camera on a tripod as close to the window as is practical. Ideally, the sun should be behind the camera, which may affect which window you choose to use for this project. If the sun is directly behind the bird, you will get only silhouettes of birds, which are not very gratifying. The window should be thoroughly cleaned inside and out. Make sure there are no reflections in the area of the window through which you are shooting. If the end of the lens is very close to the window, there should not be any reflections in the images. Adjust room lighting if necessary. Even double-paned windows should have little noticeable effect on image quality.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F1V/1SRU/KY8P62DF/F1V1SRUKY8P62DF.jpg?auto=webp&frame=1&width=790&fit=bounds&md=074ac899fc620af930e3b9d8c36e2332",
    )

    slowmo_bird2=Instruction(
        projectId=6,
        stepOrder=2,
        stepTitle="The Photography",
        instructions="""
                        Equipment

                        The camera must have some degree of manual controls. Almost any DSLR will do, and many superzoom point-and-shoot cameras will also work (my equipment is detailed in a photo above). The length of the lens required depends on how far the feeder is from the window. If the feeder is far away, a longer, presumably more expensive lens will be needed. The tripod doesn't need to be fancy, as long as it holds the camera firmly.

                        Settings

                        The camera should have Av mode, or Aperture Priority. Set the camera on this mode and adjust the aperture to F/8, or about two stops above the lowest F-stop. This setting will provide adequate depth of field and minimal aberrations. Set ISO to the lowest natural level of your camera. For example, my Canon 7D can be set as low as ISO 100, but its true minimum is 160. You should shoot on a sunny day, otherwise higher ISO will be needed and the images will become more grainy. White balance should be set on automatic or full sun. These settings work in your favor in that the camera will automatically choose the highest shutter speed that can produce a properly exposed image, resulting in freezing the motion of the bird's wings. If you have the equipment and know-how, you could set up a remote flash and probably get more consistent results, but that's beyond the scope of this Instructable.

                        Place an object halfway between the perch and the feeder and prefocus your camera on it using manual focus. Leave the camera on manual focus and try not to bump it. Set the lens at a zoom level that is reasonably wide. If you zoom it too tightly, you'll cut off bits of the birds in every frame. It's better to have the entire bird in the frame and crop it later.

                        Shooting

                        If you have one, connect a remote shutter to the camera to minimize camera shake. Set your camera on burst mode if available, and wait for a bird to land on the perch. Now place your finger on the shutter button (or remote button). As soon as the bird moves to fly, hold down the button to take a rapid series of photos (a burst). Let off the button when the bird reaches the feeder. At some point during the bird's flight, it should be in focus and in frame for at least one image. Delete the rest. It will likely require some experimentation and adjustment to get the best results. Some photographers prefer not to use burst mode, instead using their own natural skill and timing to capture a single ideal image of such a natural moment. This strategy takes considerable skill. Birds are fast!

                        Post-processing

                        It almost goes without saying that you should crop the photo and make some global lighting adjustments to make the best image you can. You may capture birds in some interesting positions. I provide a couple of examples here.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F1R/96CG/KY2ZEWJP/F1R96CGKY2ZEWJP.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=f6448db5cc082560d4f9f2019b4dc9c5",
    )

    dragonfly1=Instruction(
        projectId=7,
        stepOrder=1,
        stepTitle="Sketch and Inspiration",
        instructions="""
                        I sketched up the general idea of the bamboo dragonfly, which is exactly like the actual insect--dragonfly. I needed to model a pole for hands to hold, spin, and model a long blade as the propeller in flight. To look like a funny dragonfly, I would add a tiny head with tentacles on the top of the blade. The whole thing with all the parts assembled will be a very fantastic toy for kids.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FLY/5AIN/KSN80T48/FLY5AINKSN80T48.jpg?auto=webp&frame=1&width=860&height=1024&fit=bounds&md=bd0bbda6f38e6d64bb1c0ba4b3dc2e3d",
    )

    dragonfly2=Instruction(
        projectId=7,
        stepOrder=2,
        stepTitle="Model With Tinkercad and 3D Print",
        instructions="""
                      I used a knife to ground the blade's edges to be round and glued the tiny head to the center of the blade, which looks straight and perfect. Then I use a metal color spray to paint the whole product blue. After that, I needed to paint details of the dragonfly's eyes, stripes of its body, and the pattern of the wings with Acrylic paint. Now a vivid dragonfly comes, and it will fly in the air pushed by my hands.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FI6/SOT1/KSN80TL9/FI6SOT1KSN80TL9.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=0f94cc925b4c772cae91e777494d5583",
    )

    dragonfly3=Instruction(
        projectId=7,
        stepOrder=3,
        stepTitle="Assemble, Polish and Paint",
        instructions="""
                       I modeled the bamboo dragonfly by Autodesk Tinkercad, then export the model file with the dragonfly.STL. I opened Creality Slicer to import the Dragonfly.STL and exported to the 3D printer with file Dragonfly.gcode. So the bamboo dragonfly becomes an actual product.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FI6/SOT1/KSN80TL9/FI6SOT1KSN80TL9.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=0f94cc925b4c772cae91e777494d5583",
    )


    dragonfly4=Instruction(
        projectId=7,
        stepOrder=4,
        stepTitle="Let the Drangonfly Fly High in the Air",
        instructions="""
                       It's time to let it fly! Please watch my video.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FD5/S83I/KSN80UDF/FD5S83IKSN80UDF.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=09be231e428443e47937f1e5cabcf7fe",
        videoUrl="https://www.youtube.com/watch?v=pjgGGpcfTYQ"
    )


    db.session.add(bird_project1)
    db.session.add(bird_project2)
    db.session.add(bird_project3)
    db.session.add(bird_project4)
    db.session.add(bird_project5)
    db.session.add(casino_clock1)
    db.session.add(casino_clock2)
    db.session.add(casino_clock3)
    db.session.add(casino_clock4)
    db.session.add(casino_clock5)
    db.session.add(casino_clock6)
    db.session.add(casino_clock7)
    db.session.add(one_board_mug1)
    db.session.add(one_board_mug2)
    db.session.add(one_board_mug3)
    db.session.add(one_board_mug4)
    db.session.add(one_board_mug5)
    db.session.add(one_board_mug6)
    db.session.add(one_board_mug7)
    db.session.add(one_board_mug8)
    db.session.add(one_board_mug9)
    db.session.add(one_board_mug10)
    db.session.add(skillet_burger1)
    db.session.add(skillet_burger2)
    db.session.add(skillet_burger3)
    db.session.add(skillet_burger4)
    db.session.add(skillet_burger5)
    db.session.add(james_webb1)
    db.session.add(james_webb2)
    db.session.add(james_webb3)
    db.session.add(james_webb4)
    db.session.add(slowmo_bird1)
    db.session.add(slowmo_bird2)
    db.session.add(dragonfly1)
    db.session.add(dragonfly2)
    db.session.add(dragonfly3)
    db.session.add(dragonfly4)
    

    db.session.commit()


def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()