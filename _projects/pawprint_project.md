---
layout: page
title: PawPrint
description: An Open-Source Inertial and Magnetic Measurement Unit
img: assets/img/PawPrint/PawPrint_Logo.png
importance: 1
category: Companion Animals
related_publications: false
---

<div class="row align-items-center">
	<div class="col-8 mt-3 mt-md-0">
		<div>The PawPrint Inertial and Magnetic Measurement Unit (IMMU) is an Open-Source sensor solution that I have designed and continue to develop. The project was funded via a Research Grant awarded by the Battersea Dogs & Cats Home and sought to create a sensor solution that was as low-cost as possible while also being developed with input from both researchers and shelter staff. Alternative, more commercial solutions focus on use by animal owners and on the presentation of data visualisations that, while often familiar and intuitive due to similarities with human activity trackers, obfuscate raw data and are of limited use for more specialised use cases.</div>
	</div>
    <div class="col-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/PawPrint/Battersea_logo.jpg" title="Battersea Dogs & Cats Home Logo" class="img-fluid rounded-circle z-depth-1" %}
    </div>
</div>

<br>

<p>I initially designed the device based on a review of current trends in the literature and on my prior experiences capturing and analysing data with domestic dogs (<i>e.g.</i> <a href="https://josullivan93.github.io/projects/dogbox_project/">The DogBox project</a>), and wild animals (<i>e.g.</i> <a href="https://josullivan93.github.io/projects/baboon_project/">with Baboons</a>). It is now common for similar research devices to simultaneously capture streams of data from a diverse range of on-board sensors. To this end I included an accelerometer, gyroscope, and magnetometer on board to capture acceleration, rotation, and orientation. The PawPrint is therefore a 9 Degrees of Freedom sensor where the activity of the attached individual and its orientation over time (and relative to magnetic North) can be inferred and amalgamated to create a rich dataset for latter analysis.</p>

<p>Conversations with Battersea Shelter Staff suggested such an arrangement would be useful for the overnight monitoring of dog activity and behaviours, particularly in terms of highlighting periods of heightened activity for later viewing of CCTV cameras (avoiding arduous viewing sessions of often sleeping dogs). These conversations, alongside my own research experience, dictated the many design decisions that led to the creation of the PawPrint. For example, the use of SD-card based memory and non-board-mounted batteries were decision made both in the interest of cost (reducing replacement to a single component rather than an entire device) and practicality (hot-swapping memory and batteries for rapid redeployment and/or the relative ease of data recovery from SD when a device is damaged compared to doing so soldered flash memory).</p>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/PawPrint/schematic.png" title="Pawprint V1.1 Schematic" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    The schematic for the most recent revision of the PawPrint Sensor.
</div>

<p>Close examination of the above schematic for the most recent PawPrint (Revision 1.1) may reveal some features that have not been discussed here and are not mentioned in any documentation. As the project continued the conversations had with Battersea staff also continued. Some features discussed during these latter periods were notable and would have been included in this revision if time were unlimited. For example, staff noted the potential use of a centralised warning hub, or system that could alert staff in other areas to potential behavioural or medical issues occurring in the kennels. Such a feature would require in-depth and targeted data-collection and validation to confidently identify alert-worthy situations from IMU data and would therefore be beyond the scope of the grant. However, such a warning system, or the ability for the device to communicate and transmit signals or data with a base, was seen as potentialy highly valuable for future development.</p>

<p>Were such a feature to be included however I would opt to use the low-energy bluetooth protocols which are now prominent and have a mature list of features and applications. As an example the ability to also calculate proximity of bluetooth devices to each other through analysis of signal attenuation was considered as a potential method of networking PawPrint devices to gather social behaviour metrics inferred from this estimated proximity alongside the behavioural measures calculated from the inertial data. The groundwork for the inclusion of Bluetooth on the devices was therefore laid within the design of the 1.1 revision schematic. Similarly staff noted the potential of knowing at what times and in what ways the animals were eating/drinking, using enrichment toys <i>etc.</i> and so the potential for the attachment of an RFID reader was included in the design so passive RFID chips could be used in the future to register visits to objects and infer interaction frequency and duration when also paired with inertial sensor data.</p>

<p>My own prior research experience led to my consideration of GPS  for inclusion as it is often used alongside inertial data for "Dead-Reckoning", the reconstruction of a movement path between GPS fixes, and in applications such as geo-fencing. The exhaustive power requirements and design considerations needed for the proper utilisation of GPS made it impractical for inclusion within the project scope. However, as with Bluetooth and RFID, its potential use was considered significant enough to effectively future-proof the design for the incorporation of the feature at a later date either as part of the PawPrint or as expansion boards.</p>

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/PawPrint/gerber.png" title="PawPrint V1.1 PCB Design" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/PawPrint/pawprint_board.jpg" title="Pawprint V1.1 Final" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    The PawPrint Revision 1.1 PCB Gerber file and a photo of the final device.
</div>

<p>The final PawPrint aims and succeeds at being a cost-effective solution for 9-DoF inertial measurement with robust options for future development. The price per sensor for printing and production falls at ~£60 depending on individual component prices at time of order, significantly lower than alternatives. The size of the PawPrint device is 40mm x 35mm and fits comfortably on the collars of medium to large dogs using the custom housing that is included for 3D printing. Where small dogs are concerned the device should be fitted to a harness and wear time should be reduced so as to limit the discomfort of long-term harness wear. Where larger dogs are not comfortable with collars a harness can also be used but wear time should be limited. Software for user-friendly initialisation of the device is still in development and has not currently been released. The project remains in active development and all files and instructions can be found on the <a href="https://osf.io/kz6nw/">Open Science Framework Project Page</a>. If you have any questions regarding the PawPrint or its use please get in touch via the email or social media links at the top and bottom of this page.</p>
