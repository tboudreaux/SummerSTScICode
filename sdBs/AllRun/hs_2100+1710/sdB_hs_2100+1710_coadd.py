from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[315.77225,17.376317],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_2100+1710/sdB_hs_2100+1710_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_2100+1710/sdB_hs_2100+1710_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
