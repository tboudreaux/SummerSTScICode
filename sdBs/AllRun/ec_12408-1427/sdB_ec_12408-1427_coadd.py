from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[190.875167,-14.730344],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_12408-1427/sdB_ec_12408-1427_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_12408-1427/sdB_ec_12408-1427_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
