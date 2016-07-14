from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[278.538167,48.461081],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bd+48_2721/sdB_bd+48_2721_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bd+48_2721/sdB_bd+48_2721_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
