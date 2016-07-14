from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[203.497042,48.768753],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_BD_+49.2226/sdB_BD_+49.2226_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_BD_+49.2226/sdB_BD_+49.2226_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
