from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[224.060292,16.961278], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_145614.47+165740.6/sdB_sdssj_145614.47+165740.6_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
