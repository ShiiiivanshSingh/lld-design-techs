
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
exponential backoff
```

and probably more things will end up here because apparently implementing one design pattern is never enough.

## what's inside?

### state machine

a simple implementation of a state machine where an object moves between well-defined states based on events.

```text
IDLE
  |
 start
  ↓
RUNNING
  |
 pause
  ↓
PAUSED
  |
resume
  ↓
RUNNING
```

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

```text
        tokens
          ↓
    ┌─────────────┐
    │ TOKEN BUCKET │
    └─────────────┘
          ↓
      request
          ↓
    ┌───────────┐
    │  allowed? │
    └───────────┘
       ↓     ↓
     yes      no
      ↓        ↓
   process    reject
```

tokens are added to the bucket over time and each request consumes a token.

this is useful for:

- API rate limiting
- protecting services from traffic spikes
- controlling request frequency

---

### exponential backoff

because sometimes the server says:

> nope, try again later.

instead of retrying immediately, the client waits for an increasing amount of time between attempts.

```text
attempt 1 → fail → wait
attempt 2 → fail → wait longer
attempt 3 → fail → wait even longer
attempt 4 → success
```

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

## why did i make this?

mostly because reading:

> "use a state machine"

or

> "implement exponential backoff"

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
python rate-limiter-with-exponential-backoff.py
```

## concepts covered

```text
State Machine
Token Bucket
Rate Limiting
Exponential Backoff
Retry Logic
State Transitions
```

more will probably be added as i keep going down the LLD rabbit hole.

## made by

**shivansh**

[GitHub](https://github.com/ShiiiivanshSingh)

---

if you find something wrong, feel free to open an issue.

or don't.

i'll probably change it while you're doing that :)
