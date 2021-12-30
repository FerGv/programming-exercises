/**
 * Given a string of words, return the length of the shortest word(s).
 */

// FORM 1
// function getShortestWord(text) {
//   const wordList = text.split(' ');
//   const lenList = [];

//   for (const word of wordList) {
//     lenList.push(word.length);
//   }

//   return Math.min(...lenList);
// }

// FORM 2
const getShortestWord = (text) => Math.min(...text.split(' ').map((word) => word.length));

const text =
  'El Alquimista relata el viaje del pastor Santiago en busca de un tesoro que le había sido revelado a través de un sueño repetitivo que le mostraba';
console.log(getShortestWord(text));
