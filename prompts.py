def get_ring_prompt(programming_language: str) -> str:
    return f"""
        Below you will find the concatinated code for a ring signature library in Golang.

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


def get_smt_prompt() -> str:
    return f"""
        Below you will find the concatinated code for a sparse merkle sum trie library in Golang

        You will find that there is a `sum` that is use to determine the total
        sum of a node given the sum of all nodes in that subtree.

        My goal is to do the following: Get the total number of non-empty leaves in the tree.

        A few approaches I've thought about are:
        1. Reading directly from the underlying key-value store engine.
        2. Appending the `count` to the right of the `sum` in the node.
        3. A similar solution to (2), but using a structure that contains both `sum` and `count`.

        Take the following into consideration:
        1. It has to be simple
        2. It has to be efficient
        3. No need to over complicate things
        4. It has to be understandable
        5. It has to be cryptographically secure

        Given the code below, please do the following:
        1. Explain your suggestion
        2. Provide a short `.diff` file with a code snippet of how it would look
        3. Provide a 0.5-1 page explanation of your suggestion

        ---
    """
