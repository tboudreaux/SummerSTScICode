from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[180.477167,-17.131719],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_11593-1651/sdB_EC_11593-1651_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_11593-1651/sdB_EC_11593-1651_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
