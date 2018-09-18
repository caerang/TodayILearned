# [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## Recurrent Neural Networks

* 사람이 생각할 때 매순간 기초부터 다시 생각하지 않음
* 이전의 문맥 정보가 이후 문맥의 이해에 활용됨
* 전통적인 뉴럴넷에서는 이를 표현하기 어려움(전통적인 뉴럴넷의 단점으로 여겨짐)
* Recurrent newral networks는 이 문제를 다루고 있음
* RNN 은 뉴런 사이의 순환하는 네트워크, 정보가 영속적일 수 있도록 하는
* 정보가 현 단계에서 다음 단계의 네트워크로 전달되는 것을 가능하게 함
* 자세히 살펴 보면 일반적인 뉴럴네트워크와 다를 바 없음
* RNN 은 동일한 네트워크의 복사로 생각할 수 있음, 후대에 메시지를 전달하는
* RNN 이 시퀀스나 리스트와 관계 있음을 나타냄
* 시퀀스나 리스트와 같은 데이터를 다루기에 자연스러운 구조
* 음성인식, 언어 모델, 번역, 이미지 캡셔닝 등 다양한 문제에 응용
* LSTM 이라는 아주 특별한 RNN의 활용으로 폭발적인(?) 성능 개선을 이룸
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

사람의 사고 모델에서는 이전 정보를 활용해서 다음 정보를 해석한다. 일반적인 인공신경망은 이런 특정을 반영하지 못하는 단점을 갖고 있다. RNN 은 이런 문제를 해결하기 위한 모델이다. RNN은 동일한 인공신경망을 여러개 복재한 것으로 생각할 수 있다. 이전 노드에서 다음 노드로 정보가 전달된다. RNN 을 활용해서 음성인식, 언어 모델, 이미지 캡셔닝 등에서 성능 향상을 보였다.
LSTM은 특별한 형태의 RNN 모델이다. LSTM을 활용해서 폭발적인 성능 향상을 이뤘다.


## The Problem of Long-Term Dependencies

