/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    for(let i=0; i<nums.length; i++){
        for(let j=i+1; j<nums.length; j++){
            if(nums[i]>nums[j]){
                let t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
            }
        }
    }
    let res = []
    for(let u=0; u<nums.length; u++){
        if(nums[u]==target)
            res.push(u)
    }
    return res
};