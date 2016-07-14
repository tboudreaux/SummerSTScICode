from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[38.836542,32.149231],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0232+3155/sdB_hs_0232+3155_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0232+3155/sdB_hs_0232+3155_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
