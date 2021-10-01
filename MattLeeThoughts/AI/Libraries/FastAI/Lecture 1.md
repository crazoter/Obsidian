![[Pasted image 20211001225738.png]]

Training best done on NVIDIA GPUs
![[Pasted image 20211001232947.png]]

Another critical insight comes from considering how a model interacts with its environment. This can create _feedback loops_, as described here:

-   A _predictive policing_ model is created based on where arrests have been made in the past. In practice, this is not actually predicting crime, but rather predicting arrests, and is therefore partially simply reflecting biases in existing policing processes.
-   Law enforcement officers then might use that model to decide where to focus their police activity, resulting in increased arrests in those areas.
-   Data on these additional arrests would then be fed back in to retrain future versions of the model.

This is a _positive feedback loop_, where the more the model is used, the more biased the data becomes, making the model even more biased, and so forth.

Feedback loops can also create problems in commercial settings. For instance, a video recommendation system might be biased toward recommending content consumed by the biggest watchers of video (e.g., conspiracy theorists and extremists tend to watch more online video content than the average), resulting in those users increasing their video consumption, resulting in more of those kinds of videos being recommended. We'll consider this topic more in detail in <>.