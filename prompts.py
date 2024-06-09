def get_smt_prompt(code) -> str:
    return f"""
        Below the '~~~ code ~~~' line, you will find the concatenated code for
        a sparse merkle sum trie library in Golang.

        Your goal is to implement a solution to get the total number of non-empty
        leaves in the tree. The goal of this is to simply count the number of
        elements that were inserted into the tree.

        A few things to keep in mind as you design a solution:
        1. It has to be simple as possible, but no simpler.
        2. It has to be efficient and practical, but not over-engineered.
        3. It has to be understandable to others who may read the code.
        4. It has to be cryptographically secure.

        What to include in your solution:
        1. Provide a 1 pager explain the different approaches with tradeoffs.
        2. Provide a 1 pager explaining the solution you chose and why.
        3. Provide a complete `solution.diff` file with the result that can be
           applied via `git apply solution.diff` to the code provided.
        4. Ensure to include both the implementation and unit tests.
        5. Separate each of the above with '---' in the response you provide.

        A few approaches I've considered are are:
        1. Getting the number of key-value pairs directly from the underlying key-value
           store engine. However, this is not cryptographically secure.
        2. Appending the `count` to the right next to how `sum` is implemented.
           I didn't see any issues with it, but haven't thought about the tradeoffs.
        3. Similar to (2), but using a structure that contains both `sum` and `count`
           that is encoded using gob/encoding. This is more complex, and I felt like
           it was over-engineered.

        The suggested approaches above are just my initial ideas, but you are the
        expert, so feel free to take a different approach if you deem so.

        If there are any questions, please specify those as well alongside the
        best solution you can provide, explain and implement.

        ~~~ code ~~~

        {code}
    """


def get_ring_prompt(programming_language: str) -> str:
    return f"""
        Below you will find the concatenated code for a ring signature library in Golang.

        I received the following question:

        ```
            Question: Have you considered using a ring size 1 for such special cases? A ring of size 1 just reduces to a schnorr signature.
            I'm not 100% sure if the library would actually just work if it was used to sign/verify with a ring size of 1, but a lot of the code seems like it would still mostly work when size = 1, i = 0; c[0] = c[(i + 1) % 1] even if the execution would be rather roundabout. But a better solution would be a short-circuit to a size = 1 special-case schnorr signature that skips the ring-specific parts.
            Basically, instead of all the c[i] parts it would just be  c = challenge(ring.curve, m, l, r) and closing the ring on the single signer by calculating s = u.Sub(cx).
        ```

        Please generate a unit test, with comments that tackles the question above in {programming_language}.

        Specifically, give the code for a unit test to show that a ring size of 1 won't work.

        Here is the code:
    """
