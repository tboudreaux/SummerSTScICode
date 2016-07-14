from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[329.670667,22.498056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_2156+2215/sdB_HS_2156+2215_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_2156+2215/sdB_HS_2156+2215_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
