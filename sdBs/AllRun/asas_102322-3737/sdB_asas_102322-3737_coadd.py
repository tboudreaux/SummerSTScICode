from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[155.84125,-37.616667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_asas_102322-3737/sdB_asas_102322-3737_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_asas_102322-3737/sdB_asas_102322-3737_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
