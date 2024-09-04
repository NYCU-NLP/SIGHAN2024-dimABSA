# SIGHAN 2024 Shared Task for Chinese Dimensional Aspect-Based Sentiment Analysis (dimABSA)

Aspect-Based Sentiment Analysis (ABSA) is a critical NLP research topic that aims to identify the aspects of a given entity and analyzing the sentiment polarity associated with each aspect. In recent years, numerous research effects have been made on ABSA, which can be categorized into different tasks based on the number of sentimental elements to be extracted. For example, Aspect Sentiment Triplet Extraction (ASTE) task extracts three elements in a triplet, including aspect/target term, opinion term and sentiment polarity (e.g., positive, neutral, and negative). Furthermore, Aspect Sentiment Quadruple Prediction (ASQP) task extracts the same three elements plus an additional aspect category to construct a quadruple. However, compared to representing affective states as several discrete classes (i.e., polarity), the dimensional approach that represents affective states as continuous numerical values (called intensity) in multiple dimensions such as valence-arousal (VA) space, providing more fine-grained emotional information (Lee et al., 2022).

Therefore, we organize a Chinese dimensional ABSA shared task (dimABSA) in the SIGHAN 2024 workshop, providing fine-grained sentiment intensity prediction for each extracted aspect of a restaurant review. The four sentiment elements are defined as follows:

* <strong>Aspect Term (shorted as A): </strong>This denotes an entity indicating the opinion target. If the aspect is omitted without being mentioned clearly, we use “NULL” to represent the term.
* <strong>Aspect Category (C): </strong>This represents a predefined category for the explicit aspect of the restaurant domain. We use the same categories defined in the SemEval-2016 Restaurant dataset (Pontiki et al., 2016). There are a total of twelve categories; each can be split into an entity and attribute using the symbol “#.” We describe them as follows: “餐廳#概括” (餐厅#概括, restaurant#general), “餐廳#價格”(餐厅#价格, restaurant#prices), “餐廳#雜項” (餐厅#杂项, restaurant#miscellaneous),“食物#價格” (食物#价格, food#prices), “食物#品質” (食物#品质, food#quality), “食物#份量與款式”(食物#份量与款式, food#style&options), “飲料#價格” (饮料#价格, drinks#prices), “飲料#品質”(饮料#品质, drinks#quality), “飲料#份量與款式”(饮料#份量与款式, drinks#style&options), “氛圍#概括”(氛围#概括, ambience#general), “服務#概括” (服务#概括, services#general) and “地點#概括” (地点#概括, location#general).
* <strong>Opinion Term (O): </strong>This describes the sentiment words or phrases towards the aspects.
* <strong>Sentiment Intensity (I): </strong>This reflects respective sentiments using continuous real-valued scores in the valence-arousal dimensions. The valence represents the degree of pleasant and unpleasant (i.e., positive and negative) feelings, while the arousal represents the degree of excitement and calm. Both the valence and arousal dimensions use a nine-degree scale. Value 1 on the valence and arousal dimensions denotes extremely high-negative and low-arousal sentiment, respectively. In contrast, 9 denotes extremely high-positive and high-arousal sentiment, and 5 denotes a neutral and medium-arousal sentiment. Valence-arousal values are separated by a hashtag (symbol “#”) for a mark.

## Task Description

This task aims to evaluate the capability of an automatic system for Chinese dimensional ABSA. This task can be further divided into three subtasks described as follows.

__Subtask 1: Intensity Prediction__

The first subtask focuses on predicting sentiment intensities in the valence-arousal dimensions. Given a sentence and a specific aspect, the system should predict the valence-arousal ratings. The input format consists of ID, sentence, and aspect. The output format consists of the ID and valence-arousal predicted values that are separated with a 'space'. The intensity prediction is two real-valued scores rounded to two decimal places and separated by a hashtag, each denotes the valence and arousal rating, respectively.
```
Example 1


(Traditional Chinese version)

Input: E0001:S001, 檸檬醬也不會太油，塔皮對我而言稍軟。, 檸檬醬#塔皮

Output: E0001:S001 (檸檬醬,5.67#5.5)(塔皮,4.83#5.0)


(Simplified Chinese version)

Input: E0001:S001, 柠檬酱也不会太油，塔皮对我而言稍软。 柠檬酱#塔皮

Output: E0001:S001 (柠檬酱,5.67#5.5)(塔皮,4.83#5.0)
```

__Subtask 2: Triplet Extraction__

The second subtask aims to extract sentiment triplets composed of three elements. Given a sentence only, the system should extract all sentiment triplets (aspect, opinion, intensity). The output format consists of the ID and sentiment triplet that are separated with a 'space'.
```
Example 2


(Traditional Chinese version)

Input: E0002:S002, 不僅餐點美味上菜速度也是飛快耶！！

Output: E0002:S002 (餐點, 美味, 6.63#4.63) (上菜速度, 飛快, 7.25#6.00)


(Simplified Chinese version)

Input: E0002:S002, 不仅餐点美味上菜速度也是飞快耶!!

Output: E0002:S002 (餐点, 美味, 6.63#4.63) (上菜速度, 飞快, 7.25#6.00)
```
__Subtask 3: Quadruple Extraction__

The third subtask aims to extract sentiment quadruples composed of four elements. Given a sentence only, the system should extract all sentiment quadruples (aspect, category, opinion, intensity). The output format consists of the ID and sentiment quadruple that are separated with a 'space'.
```
Example 3


(Traditional Chinese version)

Input: E0003:S003, 這碗拉麵超級無敵霹靂難吃

Output: E0003:S003 (拉麵, 食物#品質, 超級無敵霹靂難吃, 2.00#7.88)


(Simplified Chinese version)

Input: E0003:S003, 这碗拉面超级无敌霹雳难吃

Output: E0003:S003 (拉面, 食物#品质, 超级无敌霹雳难吃, 2.00#7.88)
```
## Data Sets
We first crawled restaurant reviews from Google Reviews and an online bulletin board system PTT. Then, we removed all HTML tags and multimedia material and split the remaining texts into several sentences. Finally, we randomly selected partial sentences to retain content diversity for manual annotation.

The annotation process was conducted in two phases. We first annotated the aspect/category/opinion elements and then V#A element. In the first phase, three graduate students majoring in computer science were trained to annotate the sentences for aspect/category/opinion. One task organizer led a discussion to clarify annotation differences and seek consensus among the annotators. A majority vote mechanism was finally used to resolve any disagreements among the annotators. In the second phase, each sentence along with the annotated aspect/category/opinion was presented to five annotators majoring in Chinese language for V#A rating. Similarly, one task organizer also led a group discussion during annotation. Once the annotation process was finished, a cleanup procedure was performed to remove outlier values which did not fall within 1.5 standard deviations (SD) of the mean. These outliers were then excluded from calculating the average V#A for each instance.

We provided two versions of all datasets with identical content, but one in traditional Chinese characters and the other in simplified Chinese characters. The participating teams could choose their preferred version for the task evaluation. The submitted results were evaluated with the corresponding version of the gold standard and ranked together as the official results. 

<table class="tg"><thead>
  <tr>
    <th class="tg-baqh" colspan="10">Restaurant (REST) Domain</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-nrix" rowspan="2">   <br>Subtask </td>
    <td class="tg-nrix" rowspan="2">   <br>Dataset </td>
    <td class="tg-nrix" rowspan="2">   <br>#Sent </td>
    <td class="tg-nrix" rowspan="2">   <br>#Char </td>
    <td class="tg-nrix" rowspan="2">   <br>#Tuple </td>
    <td class="tg-baqh" colspan="3">Aspect</td>
    <td class="tg-baqh" colspan="2">Opinion</td>
  </tr>
  <tr>
    <td class="tg-baqh">#NULL</td>
    <td class="tg-baqh">#Unique</td>
    <td class="tg-baqh">#Repeat</td>
    <td class="tg-baqh">#Unique</td>
    <td class="tg-baqh">#Repeat</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="3">   <br>ST1 </td>
    <td class="tg-baqh">   <br>Train</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>6,050&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>85,769&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>8,523&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>169&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>6,430&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>1924&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>-&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>-&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-c3ow">   <br>Dev.</td>
    <td class="tg-c3ow">&nbsp;&nbsp;&nbsp;<br>100&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-c3ow">&nbsp;&nbsp;&nbsp;<br>1,109&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-c3ow">&nbsp;&nbsp;&nbsp;<br>115&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-c3ow">&nbsp;&nbsp;&nbsp;<br>0&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>115&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>0&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>-&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-c3ow">&nbsp;&nbsp;&nbsp;<br>-&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-nrix">   <br>Test</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>2,000&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>34,002&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>2,658&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>0&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>2,658&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>0&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>-&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>-&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-nrix" rowspan="3">   <br>ST2 &amp;<br>ST3 </td>
    <td class="tg-baqh">   <br>Train</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>6,050&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>85,769&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>8,523&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>169&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>6,430&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>1,924&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>7,986&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>537&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-baqh">   <br>Dev.</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>100&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>1,280&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>150&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>0&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>78&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>72&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>143&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>7&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-nrix">   <br>Test</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>2,000&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>39,014&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>3,566&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>52&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>1,693&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>1,821&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>3263&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-baqh">&nbsp;&nbsp;&nbsp;<br>303&nbsp;&nbsp;&nbsp;</td>
  </tr>
</tbody></table>

### Chinese EmoBamk
The Chinese EmoBank (Lee et al., 2022) is a dimensional sentiment resource annotated with real-valued scores for both valence and arousal dimensions. The valence represents the degree of positive and negative sentiment, and arousal represents the degree of calm and excitement. Both dimensions range from 1 (highly negative or calm) to 9 (highly positive or excited). The Chinese EmoBank features various levels of text granularity including two lexicons called Chinese valence-arousal words (CVAW, 5,512 single words) and Chinese valence-arousal phrases (CVAP, 2,998 multi-word phrases) and two corpora called Chinese valence-arousal sentences (CVAS, 2,582 single sentences) and Chinese valence-arousal texts (CVAT, 2,969 multi-sentence texts).

## Performance Matrics

For Subtask 1, the sentiment intensity prediction performance is evaluated by examining the difference between machine-predicted ratings and human-annotated ratings using two metrics: Mean Absolute Error (MAE) and Pearson Correlation Coefficient (PCC), defined as the following equations. 

$$ MAE=\frac{1}{n} \sum_{i=1}^n\mid \alpha_i - p_i \mid$$

$$ PCC=\frac{1}{n} \sum_{i=1}^n (\frac{a_i-μ_A}{σ_A})  (\frac{p_i-μ_P}{σ_P} )$$

where $a_i ∈A$ and $p_i ∈P$ respectively denote the i-th actual value and predicted value, n is the number of test samples, $μ_A$ and $σ_A$ respectively represent the mean value and the standard deviation of A, while $μ_P$ and $σ_P$ respectively represent the mean value and the standard deviation of P. 

Each metric for the valence and arousal dimensions is calculated and ranked independently. The actual and predicted real values should range from 1 to 9, so MAE measures the error rate in a range where the lowest value is 0 and the highest value is 8. A lower MAE indicates more accurate prediction performance. The PCC is a value between −1 and 1 that measures the linear correlation between the actual and predicted values. A lower MAE and a higher PCC indicate more accurate prediction performance.

For Subtasks 2 and 3, we use the F1-score as the evaluation metric, defined as:

$$ F1=\frac{2 \times P \times R}{P+R}$$

where Precision (P) is defined as the percentage of triplets/quadruples extracted by the system that are correct. Recall (R) is the percentage of triplets/quadruples present in the test set found by the system. The F1-score is the harmonic mean of precision and recall.


## Official Ranking

<table class="tg"><thead>
  <tr>
    <th class="tg-7btt" colspan="7">Subtask 1: Intensity Prediction</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-baqh" rowspan="2">Team</td>
    <td class="tg-baqh" rowspan="2">Sub#</td>
    <td class="tg-baqh" colspan="4"><span style="text-align:center">Evaluation Metrics</span></td>
    <td class="tg-baqh" rowspan="2">Overall Rank</td>
  </tr>
  <tr>
    <td class="tg-yxec">V-MAE</td>
    <td class="tg-yxec">V-PCC</td>
    <td class="tg-yxec">A-MAE</td>
    <td class="tg-yxec">A-PCC</td>
  </tr>
  <tr>
    <td class="tg-yxec">HITSZ-HLT</td>
    <td class="tg-yxec">63885</td>
    <td class="tg-7n5n"><strong>0.279</strong> (1)</td>
    <td class="tg-7n5n"><strong>0.933</strong> (1)</td>
    <td class="tg-7n5n"><strong>0.309</strong> (1)</td>
    <td class="tg-7n5n"><strong>0.777</strong> (1)</td>
    <td class="tg-yxec">1</td>
  </tr>
  <tr>
    <td class="tg-yxec">CCIIPLab</td>
    <td class="tg-yxec">63706</td>
    <td class="tg-yxec">0.294 (2)</td>
    <td class="tg-yxec">0.916 (3)</td>
    <td class="tg-7n5n"><strong>0.309</strong> (1)</td>
    <td class="tg-yxec">0.766 (3)</td>
    <td class="tg-yxec">2</td>
  </tr>
  <tr>
    <td class="tg-yxec">YNU-HPCC</td>
    <td class="tg-yxec">63756</td>
    <td class="tg-yxec">0.294 (2)</td>
    <td class="tg-yxec">0.917 (2)</td>
    <td class="tg-yxec">0.318 (3)</td>
    <td class="tg-yxec">0.771 (2)</td>
    <td class="tg-yxec">2</td>
  </tr>
  <tr>
    <td class="tg-yxec">DS-Group</td>
    <td class="tg-yxec">62014</td>
    <td class="tg-yxec">0.460 (4)</td>
    <td class="tg-yxec">0.858 (5)</td>
    <td class="tg-yxec">0.501 (4)</td>
    <td class="tg-yxec">0.490 (4)</td>
    <td class="tg-yxec">4</td>
  </tr>
  <tr>
    <td class="tg-yxec">yangnan</td>
    <td class="tg-yxec">61884</td>
    <td class="tg-yxec">1.032 (5)</td>
    <td class="tg-yxec">0.877 (4)</td>
    <td class="tg-yxec">1.095 (5)</td>
    <td class="tg-yxec">0.097 (5)</td>
    <td class="tg-yxec">5</td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-7btt" colspan="6">Subtask 2: Triplet Extraction</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-baqh" rowspan="2">Team</td>
    <td class="tg-baqh" rowspan="2">Sub#</td>
    <td class="tg-baqh" colspan="3">Evaluation Metrics</td>
    <td class="tg-baqh" rowspan="2">Overall Rank</td>
  </tr>
  <tr>
    <td class="tg-yxec">V-Tri-F1</td>
    <td class="tg-yxec">A-Tri-F1</td>
    <td class="tg-yxec">VA-Tri-F1</td>
  </tr>
  <tr>
    <td class="tg-yxec">HITSZ-HLT</td>
    <td class="tg-yxec">63885</td>
    <td class="tg-7n5n"><strong>0.589</strong> (1)</td>
    <td class="tg-7n5n"><strong>0.545</strong> (1)</td>
    <td class="tg-7n5n"><strong>0.433</strong> (1)</td>
    <td class="tg-yxec">1</td>
  </tr>
  <tr>
    <td class="tg-yxec">CCIIPLab</td>
    <td class="tg-yxec">63824</td>
    <td class="tg-yxec">0.573 (2)</td>
    <td class="tg-yxec">0.522 (2)</td>
    <td class="tg-leit">0.403 (2)</td>
    <td class="tg-yxec">2</td>
  </tr>
  <tr>
    <td class="tg-yxec">ZZU-NLP</td>
    <td class="tg-yxec">63737</td>
    <td class="tg-yxec">0.542 (3)</td>
    <td class="tg-yxec">0.507 (3)</td>
    <td class="tg-yxec">0.389 (3)</td>
    <td class="tg-yxec">3</td>
  </tr>
  <tr>
    <td class="tg-yxec">BIT-NLP</td>
    <td class="tg-yxec">63766</td>
    <td class="tg-yxec">0.490 (4)</td>
    <td class="tg-yxec">0.450 (4)</td>
    <td class="tg-yxec">0.342 (4)</td>
    <td class="tg-yxec">4</td>
  </tr>
  <tr>
    <td class="tg-yxec">SUDA-NLP</td>
    <td class="tg-yxec">63827</td>
    <td class="tg-yxec">0.475 (5)</td>
    <td class="tg-yxec">0.448 (5)</td>
    <td class="tg-yxec">0.326 (5)</td>
    <td class="tg-yxec">5</td>
  </tr>
  <tr>
    <td class="tg-yxec">TMAK-Plus</td>
    <td class="tg-yxec">63972</td>
    <td class="tg-yxec">0.269 (6)</td>
    <td class="tg-yxec">0.307 (6)</td>
    <td class="tg-yxec">0.157 (6)</td>
    <td class="tg-yxec">6</td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-7btt" colspan="6">Subtask 3: Quadruple Extraction</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-baqh" rowspan="2">Team</td>
    <td class="tg-baqh" rowspan="2">Sub#</td>
    <td class="tg-baqh" colspan="3">Evaluation Metrics</td>
    <td class="tg-baqh" rowspan="2">Overall Rank</td>
  </tr>
  <tr>
    <td class="tg-yxec"> V-Quad-F1 </td>
    <td class="tg-yxec"> A-Quad-F1 </td>
    <td class="tg-yxec"> VA-Quad-F1 </td>
  </tr>
  <tr>
    <td class="tg-yxec">HITSZ-HLT</td>
    <td class="tg-yxec">63885</td>
    <td class="tg-7n5n"><strong>0.567</strong> (1)</td>
    <td class="tg-7n5n"><strong>0.526</strong> (1)</td>
    <td class="tg-7n5n"><strong>0.417</strong> (1)</td>
    <td class="tg-yxec">1</td>
  </tr>
  <tr>
    <td class="tg-yxec">CCIIPLab</td>
    <td class="tg-yxec">63832</td>
    <td class="tg-yxec">0.555 (2)</td>
    <td class="tg-yxec">0.507 (2)</td>
    <td class="tg-leit">0.389 (2)</td>
    <td class="tg-yxec">2</td>
  </tr>
  <tr>
    <td class="tg-yxec">ZZU-NLP</td>
    <td class="tg-yxec">61868</td>
    <td class="tg-yxec">0.522 (3)</td>
    <td class="tg-yxec">0.489 (3)</td>
    <td class="tg-yxec">0.376 (3)</td>
    <td class="tg-yxec">3</td>
  </tr>
  <tr>
    <td class="tg-yxec">SUDA-NLP</td>
    <td class="tg-yxec">63622</td>
    <td class="tg-yxec">0.487 (4)</td>
    <td class="tg-yxec">0.444 (4)</td>
    <td class="tg-yxec">0.336 (4)</td>
    <td class="tg-yxec">4</td>
  </tr>
  <tr>
    <td class="tg-yxec">JN-NLP</td>
    <td class="tg-yxec">63572</td>
    <td class="tg-yxec">0.482 (5)</td>
    <td class="tg-yxec">0.439 (5)</td>
    <td class="tg-yxec">0.331 (5)</td>
    <td class="tg-yxec">5</td>
  </tr>
  <tr>
    <td class="tg-yxec">BIT-NLP</td>
    <td class="tg-yxec">63766</td>
    <td class="tg-yxec">0.470 (6)</td>
    <td class="tg-yxec">0.434 (7)</td>
    <td class="tg-yxec">0.329 (6)</td>
    <td class="tg-yxec">6</td>
  </tr>
  <tr>
    <td class="tg-yxec">USTC-IAT</td>
    <td class="tg-yxec">63907</td>
    <td class="tg-yxec">0.438 (7)</td>
    <td class="tg-yxec">0.437 (6)</td>
    <td class="tg-yxec">0.312 (7)</td>
    <td class="tg-yxec">7</td>
  </tr>
</tbody></table>




## Citation


Lung-Hao Lee, Liang-Chih Yu, Suge Wang, and Jian Liao. 2024. Overview of the SIGHAN 2024 Shared Task for Chinese Dimensional Aspect-Based Sentiment Analysis. In *Proceedings of the 10th SIGHAN Workshop on Chinese Language Processing*, pp. 165-174.https://aclanthology.org/2024.sighan-1.19/

@ARTICLE{Lee-SIGHAN-2024,<br>
&emsp;&emsp;&emsp;&emsp;author  = {Lung-Hao Lee, Liang-Chih Yu, Suge Wang, and Jian Liao},<br>
&emsp;&emsp;&emsp;&emsp;title   = {Overview of the SIGHAN 2024 Shared Task for Chinese Dimensional Aspect-Based Sentiment Analysis},<br>
&emsp;&emsp;&emsp;&emsp;proceedings = {Proceedings of the 10th SIGHAN Workshop on Chinese Language Processing},<br>
&emsp;&emsp;&emsp;&emsp;pages   = {165-174},<br>
&emsp;&emsp;&emsp;&emsp;month   = aug,<br>
&emsp;&emsp;&emsp;&emsp;year    = 2024,<br>
&emsp;&emsp;&emsp;&emsp;url     = {https://aclanthology.org/2024.sighan-1.19/}<br>
}   

## Reference

Lung-Hao Lee, Jian-Hong Li and Liang-Chih Yu. 2022. Chinese EmoBank: Building valence-arousal resources for dimensional sentiment analysis. ACM Transactions on Asian and Low-Resource Language Information Processing, 21(4), Article 65, 18 pages. https://doi.org/10.1145/3489141

