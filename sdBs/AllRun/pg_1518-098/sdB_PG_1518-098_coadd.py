from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[230.24725,-9.982194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1518-098/sdB_PG_1518-098_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1518-098/sdB_PG_1518-098_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
