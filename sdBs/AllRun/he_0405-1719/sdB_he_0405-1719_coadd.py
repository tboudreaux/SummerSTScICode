from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[61.86475,-17.187639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_0405-1719/sdB_he_0405-1719_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_0405-1719/sdB_he_0405-1719_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
