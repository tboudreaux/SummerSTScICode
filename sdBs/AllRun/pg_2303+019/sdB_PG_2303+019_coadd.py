from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[346.593167,2.151714],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_2303+019/sdB_PG_2303+019_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_2303+019/sdB_PG_2303+019_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
