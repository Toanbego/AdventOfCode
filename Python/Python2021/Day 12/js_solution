import run from "aocrunner";

type Cave = string;
type Path = Cave[];
type Input = {
  [cave: Cave]: Cave[];
};
const caveEdgesExamples = {
  start: ["A", "b"],
  A: ["c", "b", "start"],
};

const testIn = `start-A
start-b
A-c
A-b
b-d
A-end
b-end`;

const parseInput = (rawInput: string): Input => {
  const caveEdges: Input = {};

  // Populate all caves
  rawInput
    .split("\n")
    .flatMap((x) => x.split("-"))
    .forEach((cave) => {
      caveEdges[cave] = [];
    });

  // Populate edges
  rawInput.split("\n").forEach((line) => {
    const [from, to] = line.split("-");
    caveEdges[from].push(to);
    caveEdges[to].push(from);
  });

  return caveEdges;
};

const isBigCave = (cave: Cave) => cave === cave.toUpperCase();
// isBigGave('a') -> a === A -> false
// isBigGave('A') -> A === A -> true

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const edges = input;

  // Path er hvor iteration path har vært
  const canVisit = (path: Cave[], nextCave: Cave) =>
    !path.includes(nextCave) || isBigCave(nextCave);

  const traverse = (currentCave: Cave, pathSoFar: Cave[]): Path[] => {
    if (!canVisit(pathSoFar, currentCave)) return [];

    const currentPath = [...pathSoFar, currentCave];
    if (currentCave === "end") {
      return [currentPath];
    }

    let possiblePaths: Path[] = [];
    for (let nextCave of edges[currentCave]) {
      const possiblePathsWithNextCave = traverse(nextCave, currentPath);
      possiblePaths = [...possiblePaths, ...possiblePathsWithNextCave];
    }

    return possiblePaths;
  };

  const paths = traverse("start", []);
  return paths.length;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  const edges = input;

  interface SpecialSmallCave {
    readonly cave: Cave;
    readonly visitCount: number;
  }

  const canVisit = (
    path: Cave[],
    nextCave: Cave,
    specialSmallCave: SpecialSmallCave,
  ) => {
    if (isBigCave(nextCave)) return true;
    if (nextCave === specialSmallCave.cave && specialSmallCave.visitCount < 2)
      return true;
    if (!path.includes(nextCave)) return true;
    return false;
  };

  const traverse = (
    currentCave: Cave,
    pathSoFar: Cave[],
    specialSmallCave: SpecialSmallCave,
  ): Path[] => {
    if (!canVisit(pathSoFar, currentCave, specialSmallCave)) return [];

    const currentSpecialSmallCave = { ...specialSmallCave };
    if (currentCave === specialSmallCave.cave) {
      currentSpecialSmallCave.visitCount++;
    }

    const currentPath = [...pathSoFar, currentCave];
    if (currentCave === "end") {
      return [currentPath];
    }

    let possiblePaths: Path[] = [];
    for (let nextCave of edges[currentCave]) {
      const possiblePathsWithNextCave = traverse(
        nextCave,
        currentPath,
        currentSpecialSmallCave,
      );
      possiblePaths = [...possiblePaths, ...possiblePathsWithNextCave];
    }

    return possiblePaths;
  };

  const smallCaves = Object.keys(edges).filter(
    (cave) => !isBigCave(cave) && cave !== "start" && cave !== "end",
  );

  const paths = smallCaves
    .map((smallCave) =>
      traverse("start", [], { cave: smallCave, visitCount: 0 }),
    )
    .flat()
    .map((path) => path.join(""));

  const uniquePaths = new Set(paths);

  return uniquePaths.size;
};

const testInput1 = `start-A
start-b
A-c
A-b
b-d
A-end
b-end`;
const testInput2 = `dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc`;

const testInput3 = `fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW`;

run({
  part1: {
    tests: [
      { input: testInput1, expected: 10 },
      { input: testInput2, expected: 19 },
      { input: testInput3, expected: 226 },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      { input: testInput1, expected: 36 },
      { input: testInput2, expected: 103 },
      { input: testInput3, expected: 3509 },
    ],
    solution: part2,
  },
  trimTestInputs: true,
});
