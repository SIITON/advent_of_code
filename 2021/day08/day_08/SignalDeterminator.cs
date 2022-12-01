using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day_08
{
    public class SignalDeterminator
    {
        public List<string> Input { get; set; }

        public int DecodeByLength(Func<int, bool> func)
        {
            var count = 0;
            foreach (var sequence in Input)
            {
                var signalPattern = sequence.Split("|")[1].Split(" ").ToList();
                foreach (var signal in signalPattern)
                {
                    if (func(signal.Length))
                    {
                        count++;
                    }
                }
            }

            return count;
        }

        /*
             a a a
            f     b
            f     b
             g g g
            e     c
            e     c
             d d d
        */
        public List<int> Decode()
        {
            foreach (var sequence in Input)
            {
                var signal = sequence.Split("|");
                var uniquePattern = signal[0].Split(" ").ToList();
                var digitsToDecode = signal[1].Split(" ").ToList();

                var numbers = new List<string>
                {
                    string.Empty,
                    uniquePattern.First(s => s.Length is 2),
                    string.Empty,
                    string.Empty,
                    uniquePattern.First(s => s.Length is 4),
                    string.Empty,
                    string.Empty,
                    uniquePattern.First(s => s.Length is 3),
                    uniquePattern.First(s => s.Length is 7),
                    string.Empty,
                };

                var numberZeroSixNine = uniquePattern.Where(s => s.Length is 6);
                var numberTwoThreeFive = uniquePattern.Where(s => s.Length is 5);
                //var numberThree = numberTwoThreeFive.First(s => s.Contains(numberOne));
                foreach (var num in numberZeroSixNine)
                {
                    var numAsEnumerable = num.AsEnumerable();
                    var numberOne = numbers[1].AsEnumerable();

                    var union = numAsEnumerable.Union(numberOne);
                    if (union.Count() - 5 == 1)
                    {
                        numbers[6] = num;
                    }

                    var anotherUnion = numAsEnumerable.Union(numbers[4]);



                }
                //numbers[3] = numberTwoThreeFive.First(s => s.Contains(numbers[1].AsEnumerable().ToList()));

                // Number five contains the difference between 4 and 1.
                var diff = (numbers[4] + numbers[1]).Distinct().ToString();
                //var numberFive = numberTwoThreeFive.First(s => s.Contains()))
            }

            return new List<int>();
        }
    }
}
