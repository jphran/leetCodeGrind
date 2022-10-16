"""
Notes:
    - interviewer is late
    -
"""


class Type:
    def __init__(self, name: str) -> None:
        self.name = name


class TypeAlias:
    def __init__(self, new_name: str, old_name: str) -> None:
        self.new_name = new_name
        self.old_name = old_name


def resolve_type_aliases(
    types: list[Type], type_aliases: list[TypeAlias]
) -> dict[str, Type]:
    """
    M is the size of types
    N is the size of type_aliases
    K is the max number of type aliases of a single type
    space complexity: O(M + N)
    time complexity: O(M + N * K)
    """
    # validity check
    if not types and type_aliases:
        raise ValueError

    resolved_alias = {t.name: t for t in types}  # time: O(M), space O(M)
    old_type_by_new_type = {
        t.new_name: t.old_name for t in type_aliases
    }  # time: O(N), space O(M)

    # time: O(NK) only need to cycle through max depth alias once assuming
    # no aliased, aliases
    # space: O(K)
    for type_alias in type_aliases:
        alias_name = type_alias.new_name
        children_alias: list[str] = []
        while alias_name not in resolved_alias:
            children_alias.append(alias_name)
            alias_name = old_type_by_new_type[alias_name]

        t = resolved_alias[alias_name]
        for child in children_alias:
            resolved_alias[child] = t

    return resolved_alias


if __name__ == "__main__":
    types = [Type("Foo"), Type("Baz"), Type("Kar")]
    aliases = [
        TypeAlias("Quux", "Bar"),
        TypeAlias("Bar", "Foo"),
        TypeAlias("Dim", "Kar"),
        TypeAlias("Jay", "Baz"),
        TypeAlias("X", "Quux"),
    ]
    print(resolve_type_aliases(types, aliases))
