from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[234.530875,27.695442],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1536+278/sdB_PG_1536+278_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1536+278/sdB_PG_1536+278_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
