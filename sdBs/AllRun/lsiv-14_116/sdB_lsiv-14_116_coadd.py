from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[314.411917,-14.428339],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lsiv-14_116/sdB_lsiv-14_116_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lsiv-14_116/sdB_lsiv-14_116_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
