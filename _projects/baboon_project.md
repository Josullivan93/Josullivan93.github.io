---
layout: page
title: Baboon Project
description: Assessing the use of machine learning for monitoring baboon raiding behaviours. Photo Credit&#58; Gaëlle Fehlmann.
img: assets/img/baboon/baboonPhoto.png
importance: 1
category: Wild Animals
related_publications: true
---

<p>While undertaking my Master's of Research at Swansea University I was a member of the <a href="https://www.shoalgroup.org/">SHOAL Group</a> and my thesis ("The applicability of animal-attached tri-axial accelerometers and machine learning techniques for inferring the behaviour of wild social primates") explored the use of remote sensing (namely the accelerometer) in the automated classification of behaviours in the Chacma Baboon. Here I annotated footage of the wild population of baboons, identified a range of potentially informative behaviours, and assessed the utility of a diverse number of machine learning algorithms in the accurate and reliable classification of these behaviours.</p>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/baboon/baboonPhoto.png" title="Baboon with tag attached" class="img-fluid rounded z-depth-1" %}
    </div>
	<div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/baboon/baboon_collar.png" title="Diagram of attachment method, location & orientation." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Baboon diagram and photo. Photo Credit: Gaëlle Fehlmann.
</div>

<p>This work formed a foundation which was then further refined by the SHOAL group team (particularly the PhD student whose project it was: <a href="https://fehlmanng.com/">Dr. Gaelle Fehlmann</a>) after the completion of my masters. The paper resulting from this {% cite fehlmann2017identification %} presents a validated end-to-end methodology for the use of collar-mounted accelerometers, alongside random forest models of classification, for the remote identification of baboon behaviours. This method is presented in detail to inspire future work exploring novel questions of primate behavioural ecology without requiring extensive, disruptive observation, handling and/or habituation of wild primates. The works' focus on grooming behaviours underlines the potential of this, and similar methods, for the future assessment of social interactions and networks within groups. This adds to a wealth of literature exploring the exciting prospect of the use of diverse biotelemetry sensors and methodologies to capture longitudinal datasets that could better allow researchers the ability to model complex social group interactions, roles, and decision making.</p>

<div class="container-fluid text-center mt-4 p-0">
    <div class="col-sm mt-3 mt-md-0 d-flex justify-content-center">
        {% include figure.liquid path="assets/img/baboon/baboon_workflow.png" title="Diagram of behaviour annotation/identification workflow." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption text-left">
    Diagram of behaviour annotation/identification workflow {% cite fehlmann2017identification %}.
</div>
