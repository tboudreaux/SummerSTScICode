from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[218.089542,-22.657108],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HD_127493/sdB_HD_127493_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HD_127493/sdB_HD_127493_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
