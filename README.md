<div align="center">

![LLD Design Techs](https://capsule-render.vercel.app/api?type=transparent&height=100&color=gradient&text=lld%20design%20techs&animation=fadeIn&textBg=false)

A tiny collection of **low-level design patterns and system design concepts**, implemented in Python.

<br>

<img width="1280" height="720" alt="rate limiter w token bucket rate limiter w sliding window rate limiter w exponential backoff finite state machine" src="https://github.com/user-attachments/assets/06fd6454-262e-4fd9-85e7-63649409e5ee" />

</div>

<br>

## what is this?

this repo is basically my little playground for understanding **low-level design and common system design building blocks** by actually implementing them instead of just reading about them.

nothing too fancy.

just small, focused Python implementations of concepts that show up a lot in backend systems, interviews, and real-world applications.

currently, the repo includes:

```text
state machine
token bucket rate limiter
sliding window counter
exponential backoff
```

and probably more things will end up here because apparently implementing one design pattern is never enough.

## what's inside?

### state machine

a simple implementation of a state machine where an object moves between well-defined states based on events.

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/24f8306e-7e91-47a2-9c21-3e11f8864bed"
    width="500"
    alt="state machine"
  />
</p>




it demonstrates how to:

- define states
- define valid transitions
- handle events
- reject invalid transitions

useful whenever an object's behavior depends on its current state.

---

### token bucket rate limiter

a simple **token bucket** implementation for controlling how frequently requests can be made.

the basic idea:

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/1dc322c7-64b2-4d9d-a8d3-fca0ef3fa018"
    width="450"
    alt="token bucket rate limiter"
  />
</p>



tokens are added to the bucket over time and each request consumes a token.

this is useful for:

- API rate limiting
- protecting services from traffic spikes
- controlling request frequency

---

### sliding window counter

another approach to rate limiting that keeps track of requests in the **current window** and uses the previous window as a weighted estimate.

instead of treating every fixed window equally, the previous window is gradually given less weight as time moves forward.

<p align="center">
  <img
    src="https://github.com/user-attachments/assets/3abb6e31-48c2-4f7c-8eba-0d8021fbabc5"
    width="500"
    alt="sliding window counter"
  />
</p>

the estimated request count is calculated roughly as:

```text
estimated count =
current requests
+ previous requests × remaining window weight
```

for example:

```text
previous = 5
current  = 2
weight   = 0.4

count = 2 + (5 × 0.4)
      = 4
```

if the estimated count reaches the configured limit, the request is rejected.

this approach helps smooth out the sharp boundaries that can happen with a simple fixed-window counter.

---

### exponential backoff

because sometimes the server says:

> nope, try again later.

instead of retrying immediately, the client waits for an increasing amount of time between attempts.

<!-- <img width="3919" height="183" alt="exponential_backoff" src="https://github.com/user-attachments/assets/2414f254-1894-4476-9e66-a37c31ea8d5b" /> -->

<img width="5311" height="635" alt="exponential_backoff_v2" src="https://github.com/user-attachments/assets/2ddc540a-77ab-4332-96bf-f6b3ff131832" />



the delay generally grows exponentially:

```text
1s
2s
4s
8s
...
```

the implementation also includes a maximum delay so things don't get ridiculous.

this pattern is commonly used when dealing with:

- temporary network failures
- overloaded services
- external APIs
- distributed systems

---

## why did i make this?

mostly because reading:

> "use a state machine"

or

> "implement a rate limiter"

is very different from actually sitting down and writing one.

so this repo is basically me turning those concepts into small working implementations.

the goal is to keep each example:

```text
small
readable
runnable
easy to modify
```

rather than building unnecessarily complicated frameworks around simple ideas.

## structure

```text
lld-design-techs/
│
├── state-machine.py
│
├── rate-limiter-token-bucket.py
│
├── rate-limiter-sliding-window.py
│
├── rate-limiter-with-exponential-backoff.py
│
└── README.md
```

## running the examples

all implementations are written in Python.

clone the repo:

```bash
git clone https://github.com/ShiiiivanshSingh/lld-design-techs.git
cd lld-design-techs
```

then run whichever example you want:

```bash
python state-machine.py
```

```bash
python rate-limiter-token-bucket.py
```

```bash
python rate-limiter-sliding-window.py
```

```bash
python rate-limiter-with-exponential-backoff.py
```

## concepts covered

```text
State Machine

Token Bucket
Rate Limiting
Sliding Window Counter

Exponential Backoff
Retry Logic

State Transitions
```

more will probably be added as i keep going down the LLD rabbit hole.

---

if you find something wrong, feel free to open an issue.

or don't.

i'll probably change it while you're doing that :)
