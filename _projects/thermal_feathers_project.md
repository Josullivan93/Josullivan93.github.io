---
layout: page
title: Thermal Feathers
description: A rapid welfare assessment tool for commercial poultry farms.
img: assets/img/Thermal_Feathers/thermography.jpg
importance: 2
category: Commercial Animals
---

<p>The monitoring of commercial poultry welfare relies predominately on in-person assessments performed during regular "walkthrough" inspections of flocks. Despite the collection of extensive records of qualitative indicators of health and welfare, the stocking densities of commercial flocks and the time constraints on staff create challenges in the reliable recognition of early signs of welfare degradation. These indicators of negative health and welfare could be particularly subtle or occur in a only a few birds.</p>

<p>One measure staff members are required to collect on sub-samples of birds, as they perform their walkthroughs, is the feather score. The feather score is a scale describing levels of feather cover that birds are assessed and scored against. Feather cover is an important indicator of many issues such as; undesirable flock behaviours, stress, pain, injury, or insufficient husbandry. The earlier trends of decreasing feather cover can be captured and acted upon the more likely it is that issues can be corrected. This is important as causal injuries or behaviours can often result in increased flock mortality, and sufficient feather cover is vital for the fulfillment of both behavioural and physiological functions (the absence of which could again result in increased mortality).</p>

<p>This project investigated the utility of thermography as an alternative to qualitative feather scoring. The increasing availability thermographic sensors in forms that are hand-held or attach directly to modern smartphones (such as the FLIR One) allows for the affordable and practical capture of thermal imaging when performing walkthroughs. I assisted in the development of a prototype Java based application that captured and processed the thermographic image data of a chicken, using the Canny Edge Detection method as implemented in the OpenCV library. Feather scores were recorded alongside thermal images and data were explored to identify thermographic summary statistics able to accurately reflect recorded feather scores. The app then had these models incorporated at runtime to produce a rapid score result once an image was taken, alongside measured temperature.</p>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Thermal_Feathers/flirone.png" title="Phone and attached Flir One Thermographic Camera" class="img-fluid rounded z-depth-1" %}
    </div>
	<div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/Thermal_Feathers/AppDemo.png" title="Demo image of Thermal Feathers Application" class="img-fluid rounded z-depth-1" width="50%" %}
    </div>
</div>
<div class="caption">
    A FLIR One thermographic camera and phone & A demonstrative image of the application - The top images are live feeds of visual and thermal data, the bottom are the thermal image captured and the edge detected "chicken" for operator appraisal.
</div>

<p>This project focussed on feather-scoring as a qualitative measure which could see significant benefits from the introduction of quantative alternatives. However, the ease of use and increasingly mangeable form factors allows for the expansion of thermographic work within commercial poultry farming to go further. Thermographic measures are increasingly used in the detection of inflammation, injury, illness (and recovery) and, even the inference of and individuals affective state. A more diverse tool is therefore an additional possibility as is the potential to take these methods that have been explored within commercial settings to non-commercial, wild or domestic, birds and assess their utility within these substantially different contexts with distinct challenges.</p>
