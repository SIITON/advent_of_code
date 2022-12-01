using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day_14
{
    public class SubmarineEquipment
    {
        private string _template;
        private readonly List<string> _recipes;
        private Dictionary<string, long> _countsOf;

        public SubmarineEquipment()
        {
            _template = "BCHCKFFHSKPBSNVVKVSK";
            _recipes =
                File.ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day14\\day_14\\input.txt").ToList();

            // test:
            //_template = "NNCB";
            //_recipes =
            //    File.ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day14\\day_14\\testinput.txt").ToList();

            _countsOf = new Dictionary<string, long>();
            for (int i = 0; i < _template.Length - 1; i++)
            {
                var pair = _template[i] + _template[i + 1].ToString();
                if (!_countsOf.ContainsKey(pair))
                {
                    _countsOf.Add(pair, 1);
                }
                else
                {
                    _countsOf[pair] += 1;
                }
                
            }

        }
        public void FindPolymerByInsertion()
        {
            for (int i = 0; i < 10; i++)
            {
                var polymer = GrowPolymer(_template);
                _template = polymer;
            }

            var result = _template.AsEnumerable().OrderByDescending(e => e).ToList();
            foreach (var element in result.Distinct())
            {
                Console.WriteLine($"{element} appears {result.Where(e => e.Equals(element)).Select(e => e).Count()} times.");
            }
        }
        private string GrowPolymer(string template)
        {
            // BCHC -> BCCNHSC
            var result = template[0].ToString();
            for (int i = 0; i < template.Length - 1; i++)
            {
                var pair = template[i] + template[i + 1].ToString();
                var element = _recipes.Where(r => r.StartsWith(pair)).Select(r => r.Last().ToString()).First();
                result += element + template[i + 1];
            }

            return result;
        }

        public Dictionary<char, long> FindPolymerCounts()
        {
            var charCounts = new Dictionary<char, long>();
            for (int i = 0; i < 40; i++)
            {
                // BC -> (BN, NC) ty BC -> N
                var countsOf = new Dictionary<string, long>();
                foreach (var pairKeys in _countsOf.Keys.ToList())
                {
                    var element = _recipes.Where(r => r.StartsWith(pairKeys)).Select(r => r.Last().ToString()).First();
                    if (!countsOf.ContainsKey(pairKeys[0] + element))
                    {
                        countsOf.Add(pairKeys[0] + element, _countsOf[pairKeys]);
                    }
                    else
                    {
                        countsOf[pairKeys[0] + element] += _countsOf[pairKeys];
                    }

                    if (!countsOf.ContainsKey(element + pairKeys[1]))
                    {
                        countsOf.Add(element + pairKeys[1], _countsOf[pairKeys]);
                    }
                    else
                    {
                        countsOf[element + pairKeys[1]] += _countsOf[pairKeys];
                    }
                }
                _countsOf = new Dictionary<string, long>(countsOf);
            }

            // Count characters
            foreach (var pair in _countsOf)
            {
                var firstLetter = pair.Key[0];
                if (!charCounts.ContainsKey(firstLetter))
                {
                    charCounts.Add(firstLetter, _countsOf[pair.Key]);
                }
                else
                {
                    charCounts[firstLetter] += _countsOf[pair.Key];
                }
            }
            // Add last character
            charCounts[_template.Last()] += 1;

            return charCounts;
        }
    }
}
