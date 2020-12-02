package com.Torstein;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day1 {

    public static void main(String[] args) throws FileNotFoundException {
        List<Integer> expenses = new ArrayList<Integer>();
        int goal = 2020;
        // Create a scanner object to open the input file
        Scanner inFile = new Scanner(new File("Day1_input/puzzle_input.txt")).useDelimiter("\n");
        while (inFile.hasNext()) {
            expenses.add(Integer.parseInt(inFile.nextLine()));
        }
        Result result = (Result) solveTwoSumProblem(expenses, goal);
        assert result != null;
        System.out.println(result.getFirst() * result.getSecond());

        Result result_2 = (Result) solveThreeSumProblem(expenses, goal);
        System.out.println(result_2.getFirst() * result_2.getSecond() * result_2.getThird());
    }


    private static Object solveTwoSumProblem(List<Integer> expenses, int goal) {
        int number_required_for_goal;
        int number2;
        int number3 = 0;
        Result result;
        for (int number1: expenses){
                number_required_for_goal = goal - number1;
                if (expenses.contains(number_required_for_goal)) {
                    number2 = expenses.get(expenses.indexOf(number_required_for_goal));
                    return new Result(number1, number2, number3);
                }
        }
        return null;
    }
    private static Object solveThreeSumProblem(List<Integer> expenses, int goal) {
        int number_required_for_goal;
        for (int number: expenses){
            number_required_for_goal = goal - number;
            Result temp_res = (Result) solveTwoSumProblem(expenses, number_required_for_goal);
            if (temp_res != null) {
                return new Result(temp_res.getFirst(), temp_res.getSecond(), number);
            }
        }
        return null;
    }
}

final class Result {
    private final int nr1;
    private final int nr2;
    private final int nr3;
    public Result(int nr1, int nr2, int nr3) {
        this.nr1 = nr1;
        this.nr2 = nr2;
        this.nr3 = nr3;
    }
    public int getFirst() {
        return nr1;
    }
    public int getSecond() {
        return nr2;
    }
    public int getThird() {
        return nr3;
    }
}