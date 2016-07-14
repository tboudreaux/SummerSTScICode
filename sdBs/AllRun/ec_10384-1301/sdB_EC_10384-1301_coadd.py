from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[160.220333,-13.292556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_10384-1301/sdB_EC_10384-1301_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_10384-1301/sdB_EC_10384-1301_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
