---
layout: page
title: Gaitkeeper
description: Canine pedometer & gait kinematics for veterinary monitoring.
img: assets/img/gaitkeeper/Project_Dog.png
importance: 3
category: Companion Animals
related_publications: true
---

<p>Immediately prior to my PhD I worked on a couple of projects in partnership with VetSens - a company local to Newcastle-Upon-Tyne exploring the utility of accelerometers in the assessment of gait of quadruped companion animals.</p>

<p>The first of these was the GaitKeeper System {% cite ladha2017gaitkeeper %}. Gaitkeeper was conceived as a quantitative tool to be used during veterinary gait assessment that was more both more affordable and practical than the current gold standard of force plates and/or manual or computer-vision based video coding. Such systems are ubiquitous in human movement research and are seeing increased use in equine veterinary research and practice. Mimicking this prior work, particularly that performed with horses, and to accurately assess the relative acceleration and impact of each leg, sensors were attached directly to the 4 limbs (above the carpal joints of the thoracic limbs and below the tarsal joints of the pelvic limbs). The data collected in this way, following the signal processing methodology outlined in the paper, allowed for the detection of gait features (such contact times), and was robust to size differences across diverse breeds and conformations. The Gaitkeeper system, and by extension similar accelerometer-based methods, shows promise as a future tool in the identification of clinically relevant gait abnormalities in dogs. With further validation, and considering the clinical ubiquity of similar systems in human medicine, a refined Gaitkeeper system could provide vital insight into aspects of canine gait currently difficult to quantify without expensive or impractical insturmentation.</p>

<div class="row justify-content-sm-center">
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/gaitkeeper/DogLegAX3.png" title="Attaching the Axivity AX3 to a dogs leg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/gaitkeeper/gaitkeeper_orientation.png" title="Axivity Sensor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Gaitkeeper accelerometer attachement location & orientation diagram.
</div>

<p>The second of these projects {% cite ladha2018step %} took a different approach for the objective measurement of canine gait features. Instead of individual step or stride events per foot (as with Gaitkeeper) it focussed on the detection of overall step numbers and resulting distance travelled using a collar mounted sensor. Collar-based pedometers like this are common in the marketplace but often use "closed-source" or black-box algorithms that are inaccessible to researchers. The method outlined in the paper addresses the idiosyncracies of canine gait and is entirely open-source. The resulting measures of step count and distance may be advantageous for the use in physical activity detection and classification, or in the "dead-reckoning" of locomotion paths where GPS signals are obscured (such as inside buildings) or battery longevity is a concern (as GPS is battery intensive).</p>

<div class="container-fluid text-center mt-4 p-0">
    <div class="col-sm mt-3 mt-md-0 d-flex justify-content-center">
        {% include figure.liquid path="assets/img/gaitkeeper/stepcountflow.png" title="Pedometer signal processing flow diagram" class="img-fluid z-depth-1" %}
    </div>
</div>
<div class="caption">
    Pedometer signal processing flow diagram.
</div>
