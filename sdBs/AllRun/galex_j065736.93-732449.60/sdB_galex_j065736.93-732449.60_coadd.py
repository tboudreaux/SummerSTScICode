from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[104.403875,-73.413778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j065736.93-732449.60/sdB_galex_j065736.93-732449.60_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j065736.93-732449.60/sdB_galex_j065736.93-732449.60_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
