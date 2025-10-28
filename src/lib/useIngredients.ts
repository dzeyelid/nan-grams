import type { Ingredient } from '../types/ingredient';
import { ingredients } from '../data/ingredients';

export function getAllIngredients(): Ingredient[] {
  return ingredients;
}

export function getIngredientById(id: string): Ingredient | undefined {
  return ingredients.find((ingredient) => ingredient.id === id);
}

export function filterIngredientsByTag(tag: string): Ingredient[] {
  return ingredients.filter((ingredient) => ingredient.tags.includes(tag));
}

export function getAllTags(): string[] {
  const tagSet = new Set<string>();
  ingredients.forEach((ingredient) => {
    ingredient.tags.forEach((tag) => tagSet.add(tag));
  });
  return Array.from(tagSet).sort();
}

export interface ConversionResult {
  ingredient: Ingredient;
  tablespoons: number;
  teaspoons: number;
  grams: number;
}

export function calculateGrams(
  ingredient: Ingredient,
  tablespoons: number,
  teaspoons: number
): ConversionResult {
  const grams =
    tablespoons * ingredient.gramPerTablespoon +
    teaspoons * ingredient.gramPerTeaspoon;
  
  return {
    ingredient,
    tablespoons,
    teaspoons,
    grams,
  };
}
