---
layout: page
title: Piling Detection
description: Detection of piling behaviours from video using deep learning methods.
img: assets/img/piling/chicken_prof.jpeg
importance: 1
category: Commercial Animals
related_publications: true
---

This is the current project I am involved with. Piling behaviours exhibited by commercial laying hens may result in mortalities within the flock (referred to as smothering). Piling (and by extension any resulting smothering) presents as a densely packed grouping of birds that falls into 3 categories referring to the trigger of the behaviour. These are: panic smothers, nestbox smothers, and recurring smothers. The trigger for the latter of these is unknown, with birds appearing unpanicked, and occur throughout the laying period of the hens potentially resulting in a low-level of mortality occurring throughout.

This project aims to identify these piling events through computer-vision based methods. I am currently refining and assessing a convolutional neural network to identify the occurrence of piling from CCTV videos. The development and validation of this system will allow for the identification of piling enabling producers to interrupt piling before it escalates to smothering. The rapid annotation of video data will also enable the rapid collection of future piling event data when assessing potential predictors for their impact. Further details on recurrent piling and smothering, and potential predictors can be found in {% cite gray2020hens --file other_papers --style _bibliography/intext %}.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/piling/piling.jpg" title="Diagram of piling and smothering onset" class="img-fluid z-depth-1" %}
    </div>
</div>
<div class="caption">
    Diagram of the progression of Piling/Smothering from {% cite gray2020hens --file other_papers --style _bibliography/intext %}.
</div>
